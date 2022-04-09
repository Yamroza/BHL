import pandas as pd
from sklearn import preprocessing
from sklearn.preprocessing import MinMaxScaler
import xgboost

model = xgboost.XGBRegressor('../model.json')

def prepare_data(path):
    data = pd.read_csv(path)
    data.drop(labels=["BBLE", "LOT","PERIOD", "VALTYPE",
                  "Borough", "New Georeferenced Column",
                  "OWNER", "AVLAND2", "AVTOT2",
                  "EXLAND2", "EXTOT2","BIN", "EXCD1", "EXCD2",
                  "EXMPTCL", "YEAR", "STADDR"],axis=1, inplace=True)
    data["EASEMENT"] = data["EASEMENT"].fillna("0")
    data["EXT"] = data["EXT"].fillna("0")
    data.loc[(data["EASEMENT"] == "F"), "EASEMENT"] = "E"
    data.loc[(data["EASEMENT"] == "G"), "EASEMENT"] = "E"
    data.loc[(data["EASEMENT"] == "H"), "EASEMENT"] = "E"
    data.loc[(data["EASEMENT"] == "I"), "EASEMENT"] = "E"
    data["EXT_E"] = 0
    data["EXT_G"] = 0
    data["EASEMENT_E"] = 0
    data["EASEMENT_N"] = 0
    data.loc[(data["EXT"] == "E"), "EXT_E"] = 1
    data.loc[(data["EXT"] == "EG"), "EXT_E"] = 1
    data.loc[(data["EXT"] == "G"), "EXT_G"] = 1
    data.loc[(data["EXT"] == "EG"), "EXT_G"] = 1
    data.loc[(data["EASEMENT"] == "E"), "EASEMENT_E"] = 1
    data.loc[(data["EASEMENT"] == "N"), "EASEMENT_N"] = 1
    data.drop(["EXT", "EASEMENT"], axis=1, inplace=True)
    data["STORIES"].fillna(method="ffill", inplace=True)
    data["POSTCODE"].loc[data["POSTCODE"].isnull()] = calc_postal_code(data, data["BLOCK"], "POSTCODE")
    data["Community Board"].loc[data["Community Board"].isnull()] = calc_postal_code(data, data["BLOCK"], "Community Board")
    data["Council District"].loc[data["Council District"].isnull()] = calc_postal_code(data, data["BLOCK"], "Council District")
    data["Census Tract"].loc[data["Census Tract"].isnull()] = calc_postal_code(data, data["BLOCK"], "Census Tract")
    data["NTA"].loc[data["NTA"].isnull()] = calc_district(data, data["BLOCK"], "NTA")
    data["Latitude"].loc[data["Latitude"].isnull()] = calc_average_from_block(data, data["BLOCK"], "Latitude")
    data["Longitude"].loc[data["Longitude"].isnull()] = calc_average_from_block(data, data["BLOCK"], "Longitude")
    data["STORIES"].loc[data["STORIES"].isnull()] = calc_average_from_block(data, data["BLOCK"], "STORIES")
    data = data.loc[data["FULLVAL"] != 0]
    
    le = preprocessing.OneHotEncoder()
    encoded_fit = le.fit_transform(data.BLDGCL.values.reshape(-1,1))
    encoded_fit.toarray()
    dummies = pd.get_dummies(data[["BLDGCL"]])
    data = pd.concat([data, dummies], axis = 1)
    
    encoded_fit = le.fit_transform(data.NTA.values.reshape(-1,1))
    encoded_fit.toarray()
    dummies = pd.get_dummies(data[["NTA"]])
    data = pd.concat([data, dummies], axis = 1)
    
    encoded_fit = le.fit_transform(data.TAXCLASS.values.reshape(-1,1))
    encoded_fit.toarray()
    dummies = pd.get_dummies(data[["TAXCLASS"]])
    data = pd.concat([data, dummies], axis = 1)
    
    encoded_fit = le.fit_transform(data.POSTCODE.values.reshape(-1,1))
    encoded_fit.toarray()
    dummies = pd.get_dummies(data[["POSTCODE"]])
    data = pd.concat([data, dummies], axis = 1)
    
    data.drop(labels=["BLDGCL", "NTA","TAXCLASS","POSTCODE"] ,axis=1, inplace=True)
    
#     le = preprocessing.LabelEncoder()
#     le.fit(data['BLDGCL'])
#     data.BLDGCL = le.transform(data.BLDGCL)
#     le.fit(data['NTA'])
#     data.NTA = le.transform(data.NTA)
#     le.fit(data['TAXCLASS'])
#     data.TAXCLASS = le.transform(data.TAXCLASS)
#     le.fit(data['POSTCODE'])
#     data.POSTCODE = le.transform(data.POSTCODE)
    
    sc = MinMaxScaler()
    data['Latitude'] = sc.fit_transform(data['Latitude'].values.reshape(-1,1))
    data['Longitude'] = sc.fit_transform(data['Longitude'].values.reshape(-1,1))
    data['LTFRONT'] = sc.fit_transform(data['LTFRONT'].values.reshape(-1,1))
    data['LTDEPTH'] = sc.fit_transform(data['LTDEPTH'].values.reshape(-1,1))
    data['BLDDEPTH'] = sc.fit_transform(data['BLDDEPTH'].values.reshape(-1,1))
    data['BLDFRONT'] = sc.fit_transform(data['BLDFRONT'].values.reshape(-1,1))
#     data['AVLAND'] = sc.fit_transform(data['AVLAND'].values.reshape(-1,1))
#     data['AVTOT'] = sc.fit_transform(data['AVTOT'].values.reshape(-1,1))
#     data['EXLAND'] = sc.fit_transform(data['EXLAND'].values.reshape(-1,1))
#     data['EXTOT'] = sc.fit_transform(data['EXTOT'].values.reshape(-1,1))
#     data["AVLAND"] = np.log10(data["AVLAND"].loc[data["AVLAND"] != 0])
#     data["AVTOT"] = np.log10(data["AVTOT"].loc[data["AVTOT"] != 0])
#     data["EXLAND"] = np.log10(data["EXLAND"].loc[data["EXLAND"] != 0])
#     data["EXTOT"] = np.log10(data["EXTOT"].loc[data["EXTOT"] != 0])
    data.drop(labels=["BLOCK"],axis=1, inplace=True)
    return data

def calc_average_from_block(dataset, block, column):
    new_df = dataset[dataset["BLOCK"] == block]
    return new_df[column].mean()

def calc_postal_code(data, block, column): # postcode, community board, council district, census tract
    new_df = data[data["BLOCK"] == block]
    return max(new_df[column].unique())

def calc_district(data, block, column):
    new_df = data[data["BLOCK"] == block]
    return new_df[column].unique()[0]