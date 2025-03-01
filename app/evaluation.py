import os
import openai
import json
from dotenv import load_dotenv

load_dotenv()


def evaluation_function(response, answer, params):
    """
    Function used to evaluate a student response.
    ---
    The handler function passes three arguments to evaluation_function():

    - `response` which are the answers provided by the student.
    - `answer` which are the correct answers to compare against.
    - `params` which are any extra parameters that may be useful,
        e.g., error tolerances.

    The output of this function is what is returned as the API response 
    and therefore must be JSON-encodable. It must also conform to the 
    response schema.

    Any standard python library may be used, as well as any package 
    available on pip (provided it is added to requirements.txt).

    The way you wish to structure you code (all in this function, or 
    split into many) is entirely up to you. All that matters are the 
    return types and that evaluation_function() is the main function used 
    to output the evaluation response.
    """
    openai.api_key = os.environ.get("OPENAI_API_KEY")

    prompt = "Compare the `response` to the `answer` considering the `params`. Output your answer in exactly and only the following format: \n{{\n\"command\": \"eval\",\n\"result\":{{\n\"is_correct\": \"<bool>\",\n\"feedback\":\"<string>\",\n\"warnings\": \"<array>\"\n}}\n}} \n Answer: {}. \n Response: {}. \n params: {}. \n Only provide corrective or suggestive feedback. Don't provide any subjective, emotional, or motivational feedback (such as exclamation marks or 'well done'). Don't reveal the true answer if it wasn't given in the response. Be objective. Justify the judgement.".format(
        response, answer, params)

    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=1024,
    )

    return json.loads(response["choices"][0]["text"])


if __name__ == "__main__":
    response, answer = "ketchup", "red sauce"
    print(response, answer)
    result = evaluation_function(
        response, answer, {"mode": "If the reponse is similar to the answer then the response is correct."})
    result["result"]["is_correct"] = bool(result["result"]["is_correct"])
    print(bool(result["result"]["is_correct"]))
    print(result)
