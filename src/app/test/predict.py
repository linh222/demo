from fastapi.testclient import TestClient
from app.api_key import API_KEY
from main import app

client = TestClient(app)


def test_predict_success():
    response = client.post("/v1/predict",
                           headers={"access_token": API_KEY},
                           json={
                               "lead_id": "0001",
                               "date": "2021-05-07",
                               "phone_type": "Android",
                               "telco": "VIETTEL",
                               "starting_09X": "True",
                               "starting_08X": "False",
                               "is_gmail": "True",
                               "is_yahoo_email": "False",
                               "is_educational_email": "False",
                               "package": "one_year_credit",
                               "entity_lead_source": "Organic",
                               "os_version": "Android 9",
                               "browser_type": "Safari"
                           },
                           )
    assert response.status_code == 200
    assert response.json() == {
        "lead_id": "0001",
        "lead_score": 4.67,
        "date": "2021-05-07",
        "model_version": "1.0"
    }


def test_predict_missing_auth():
    response = client.post("/v1/predict",
                           json={
                               "lead_id": "0001",
                               "date": "2021-05-07",
                               "phone_type": "Android",
                               "telco": "VIETTEL",
                               "starting_09X": "True",
                               "starting_08X": "False",
                               "is_gmail": "True",
                               "is_yahoo_email": "False",
                               "is_educational_email": "False",
                               "package": "one_year_credit",
                               "entity_lead_source": "Organic",
                               "os_version": "Android 9",
                               "browser_type": "Safari"
                           },
                           )
    assert response.status_code == 403
    assert response.json() == {'detail': 'Could not validate credentials'}
