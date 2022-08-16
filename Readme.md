OOP is first question.
train_model is second question.
model_deploy is third question. to use this one you have to implement env. to test
    - conda create -n covid-env python=3.8  
    - conda activate covid-env 
    - pip install -r requirements.txt  
    - conda install -c conda-forge pickle5
    - touch .env # if there is no .env
    - cd to model_deploy
    - uvicorn api:app --host 0.0.0.0 --port 80 --reload
    ## Test the results ##
    curl -X 'POST' \
        'http://localhost/getclass/' \
        -H 'accept: application/json' \
        -H 'Content-Type: application/json' \
        -d '{
        "text": "fear covid"
        }'