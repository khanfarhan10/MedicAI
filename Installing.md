virtualenv MedicAIEnv
MedicAIEnv\Scripts\activate
pip install -r reqs.txt
python Gen.py
python DocxGen.py

MedicAIEnv\Scripts\activate
To deactivate base - conda.bat deactivate
cd WebsiteFiles/FlaskApp