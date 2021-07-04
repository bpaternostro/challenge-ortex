class Transaction():

        def __init__(self,row) -> None:
            self.dict_transaction={
                    "transactionID":row[0],
                    "gvkey":row[1],
                    "companyName":row[2],
                    "companyISIN":row[3],
                    "companySEDOL":row[4],
                    "insiderID":row[5],
                    "insiderName":row[6],
                    "insiderRelation":row[7],
                    "insiderLevel":row[8],
                    "connectionType":row[9],
                    "connectedInsiderName":row[10],
                    "connectedInsiderPosition":row[11],
                    "transactionType":row[12],
                    "transactionLabel":row[13],
                    "iid":row[14],
                    "securityISIN":row[15],
                    "securitySEDOL":row[16],
                    "securityDisplay":row[17],
                    "assetClass":row[18],
                    "shares":row[19],
                    "inputdate":row[20],
                    "tradedate":row[21],
                    "maxTradedate":row[22],
                    "price":row[23],
                    "maxPrice":row[24],
                    "value":row[25],
                    "currency":row[26],
                    "valueEUR":row[27],
                    "unit":row[28],
                    "correctedTransactionID":row[29],
                    "source":row[30],
                    "tradeSignificance":row[31],
                    "holdings":row[32],
                    "filingURL":row[33],
                    "exchange":row[34]
            }

        def get_dict(self):
            return self.dict_transaction