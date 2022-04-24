from ctypes import Array
from random import randint
from sklearn.naive_bayes import GaussianNB
from pandas.core.frame import DataFrame

class GaussianNBManager:
    def __init__ (
            self,
            data: DataFrame,
            pressure: int,
            magnetic_storms: int = randint(3, 6)
    ):
        self.data: DataFrame = data
        self.pressure: int = pressure
        self.magnetic_storms: int = magnetic_storms

        if not self.data.empty:
            self.predicted_is_high_pressure: int = self.predict_is_high_pressure()
            self.predicted_is_head_hurts:int = self.predict_is_head_hurts()
            self.predicted_well_being: int = self.predict_well_being()

            print(
                self.predicted_is_high_pressure,
                self.predicted_is_head_hurts,
                self.predicted_well_being
            )

    def predict_is_head_hurts(self) -> int:
        model = GaussianNB()
        pressure_arr: Array = self.data["pressure"].to_numpy()
        is_head_hurts_arr: Array = self.data["is_head_hurts"].to_numpy()
        magnetic_storms_arr: Array = self.data["magnetic_storms"].to_numpy()
        
        features = list(zip(pressure_arr, magnetic_storms_arr))
        labels = is_head_hurts_arr

        model.fit(features, labels)
        result: int = model.predict(
            [(self.pressure, self.magnetic_storms)]
        ).tolist()[0]
        return result

    def predict_is_high_pressure(self) -> int:
        model = GaussianNB()
        pressure_arr: Array = self.data["pressure"].to_numpy()
        magnetic_storms_arr: Array = self.data["magnetic_storms"].to_numpy()
        is_high_pressure_arr: Array = self.data["is_high_pressure"].to_numpy()

        features = list(zip(pressure_arr, magnetic_storms_arr))
        labels = is_high_pressure_arr

        model.fit(features, labels)
        result: int = model.predict(
            [(self.pressure, self.magnetic_storms)]
        ).tolist()[0]
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
