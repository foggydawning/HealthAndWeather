from ctypes import Array
from pandas import array
from sklearn.naive_bayes import GaussianNB

class GaussianNBManager:
    def __init__(self, data: str, pressure: str):
        self.data = data
        self.pressure = pressure
        self.predicted_is_high_pressure = self.predict_is_high_pressure()
        self.predicted_is_head_hurts = self.predict_is_head_hurts()
        self.predicted_well_being = self.predict_well_being()

        print(
            self.predicted_is_high_pressure,
            self.predicted_is_head_hurts,
            self.predicted_well_being
        )

    def predict_is_head_hurts(self) -> int:
        model = GaussianNB()
        pressure_arr: Array = self.data["pressure"].to_numpy().reshape(-1, 1)
        is_head_hurts_arr: Array = self.data["is_head_hurts"].to_numpy()
        model.fit(pressure_arr, is_head_hurts_arr)
        result: int = model.predict([[self.pressure]]).tolist()[0]
        return result

    def predict_is_high_pressure(self) -> int:
        model = GaussianNB()
        pressure_arr: Array = self.data["pressure"].to_numpy().reshape(-1, 1)
        is_high_pressure_arr: Array = self.data["is_high_pressure"].to_numpy()
        model.fit(pressure_arr, is_high_pressure_arr)
        result: int = model.predict([[self.pressure]]).tolist()[0]
        return result

    def predict_well_being(self) -> int:
        model = GaussianNB()
        is_head_hurts_arr: Array = self.data["is_high_pressure"].to_numpy()
        is_high_pressure_arr: Array = self.data["is_high_pressure"].to_numpy()
        well_being_arr: Array = self.data["well_being"].to_numpy()

        features = list(zip(is_high_pressure_arr, is_head_hurts_arr))
        labels = well_being_arr

        model.fit(features, labels)
        result: int = model.predict(
            list(zip([self.predicted_is_high_pressure], [self.predicted_is_head_hurts]))
        ).tolist()[0]
        return result
