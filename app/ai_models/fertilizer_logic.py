from pandas import read_csv
import pickle
import numpy as np

def detect_deficiency(deficiency):
    column = ["N", "P", "K", "OC", "B", "Cu", "Fe", "Mn", "S", "Zn"]
    for i in range(len(column)):
        deficiency.append(df.loc[df["State/UT"] == State, column[i]].iloc[0])

    return deficiency

def fertilizer_recommendation(deficiency)
    if sample is None:
        return generalized_fertilizers(deficiency), generalized_micronutrients(deficiency)
    else:
        return ml_fertilizer(sample), generalized_micronutrients(deficiency)

def ml_fertilizer(sample):
    with open("models/fertilizer_model.pkl", "rb") as f:
        model = pickle.load(f)

    proba = model.predict_proba(sample)[0]
    classes = model.classes_
    top_indices = np.argsort(proba)[::-1][:3]
    fertilizers = {}
    for i in top_indices:
        key = classes[i]
        value = f"{round(proba[i] * 100, 2)}%"
        fertilizers[key] = value

    return fertilizers


def generalized_fertilizers(deficiency):

    N,P,K,OC = deficiency[0], deficiency[1],deficiency[2],deficiency[3]

    LOW = {"very low", "low"}
    OK = {"medium", "high", "very high"}

    low_macro = {
        "N" : N in LOW,
        "P": P in LOW,
        "K": K in LOW
    }

    low_count = sum(low_macro.values())

    fertilizer = []

    if low_count == 0:
        fertilizer.append("no fertilizer needed")

    if OC in LOW:
        if low_count == 2:
            fertilizer.append("organic matter")
            fertilizer.append("npk_complex")
        else:
            fertilizer.append("organic matter")

    elif low_count == 3:
        fertilizer.append("npk_complex")

    elif low_macro["N"] and low_macro["P"]:
        fertilizer.append("dap")

    elif low_macro["N"] and low_macro["K"]:
        fertilizer.append("npk_complex")

    elif low_macro["N"]:
        fertilizer.append("urea")

    elif low_macro["P"]:
        fertilizer.append("ssp")

    elif low_macro["K"]:
        fertilizer.append("mop")

    else:
        fertilizer.append("No recommendation")

    return fertilizer


def generalized_micronutrients(deficiency):
    micro_map = {
        "4": "zinc sulphate",
        "5": "borax",
        "6": "ferrous sulphate",
        "7": "manganese sulphate",
        "8": "copper sulphate",
        "9": "sulphur bentonite"
    }

    micronutrients = []

    for i in range(4, len(deficiency), 1):
        if deficiency[i] == "deficient":
            micronutrients.append(micro_map[str(i)])

    if micronutrients:
        return micronutrients
    else:
        micronutrients.append("no_micronutrient_needed")
        return micronutrients


def result(fertilizer, micronutrients):
    dosage = []

    for fert in fertilizer:
        if fert in dr["fertilizers"].values:
            value = dr.loc[dr["fertilizers"] == fert, "Dosage"].iloc[0]
            dosage.append({fert: value})

    for micro in micronutrients:
        if micro in dr["fertilizers"].values:
            value = dr.loc[dr["fertilizers"] == micro, "Dosage"].iloc[0]
            dosage.append({micro: value})

    return dosage


if __name__ == "__main__":
    df = read_csv("../csv datasets/state_soil_summary.csv")
    dr = read_csv("../csv datasets/dosage_recommendation.csv")
    State = "Tamil Nadu"
    sample = None

    Deficiency = detect_deficiency([])
    fertilizer, micronutrients = fertilizer_recommendation(Deficiency)
    dosage = result(fertilizer, micronutrients)