# ML Model API 🚀

This project deploys a machine learning model using Flask on AWS EC2.

## Run locally

```bash


sudo apt update
sudo apt install python3-pip python3-venv -y

python3 -m venv venv
source venv/bin/activate   // use . -> source in azure

pip install -r requirements.txt
python app.py

before that check if all the required port(5000, 8080) are added in networking.
To test:
open "reqbin.com"
add url/predict
body :
{
  "input": [5.1, 3.5, 1.4, 0.2]
}

header:
Key - Content-Type
Value - application/json

click send.

expected output : "sentosa"

