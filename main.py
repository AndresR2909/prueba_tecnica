# 1. Library imports
import uvicorn
from fastapi import FastAPI
from Modelo import ClasificadorCompras, ClasificadorComprasDatos

# 2. Create app and model objects
app = FastAPI()
model = ClasificadorCompras()

# 3. Expose the prediction functionality, make a prediction from the passed
#    JSON data and return the predicted flower species with the confidence
@app.post('/predict')
def predict_compras(datos: ClasificadorComprasDatos):
    data = datos.dict()
    prediction = model.predict_compras(
        data['autoID'],data['SeniorCity'],data['Partner'],data['Dependents'],data['Service1'],data['Service2'],data['Security'],data['OnlineBackup'],data['DeviceProtection'],data['TechSupport'],data['Contract'],data['PaperlessBilling'],data['PaymentMethod'],data['Charges'],data['Demand']
    )
    return {
        'prediction': prediction,
    }


# 4. Run the API with uvicorn
#    Will run on http://127.0.0.1:8000
if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)