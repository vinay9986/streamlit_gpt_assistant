import pandas as pd

class BaseData:
    customers: pd.DataFrame
    sales: pd.DataFrame
    alignments: pd.DataFrame

    def __init__(self,):
        customer_data = {
            'NARC': ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10'],
            'NAME': ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'],
            'Parent_NARC': ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10'],
            'Parent_NAME': ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'],
            'Address': ['Address A1', 'Address B1', 'Address C1', 'Address D1', 'Address E1', 'Address F1', 'Address G1', 'Address H1', 'Address I1', 'Address J1'],
            'City': ['City A', 'City B', 'City C', 'City D', 'City E', 'City F', 'City G', 'City H', 'City I', 'City J'],
            'State': ['State A', 'State B', 'State C', 'State D', 'State E', 'State F', 'State G', 'State H', 'State I', 'State J'],
            'Zip': ['Zip A', 'Zip B', 'Zip C', 'Zip D', 'Zip E', 'Zip F', 'Zip G', 'Zip H', 'Zip I', 'Zip J'],
            'Partner': ['Partner A', 'Partner B', 'Partner C', 'Partner A', 'Non MA/CST', 'Specialty', 'Specialty', 'Partner B', 'Non MA/CST', 'Specialty'],
            'Spec_Desc': ['None', 'None', 'None', 'None', 'None', 'Specialty Feline', 'Specialty only', 'None', 'None', 'Specialty Therapeutic'],
            'ZFS': ['Yes', 'No', 'No', 'No', 'Yes', 'No', 'Yes', 'Yes', 'Yes', 'Yes'],
        }

        customer_ids = ['10',  '3',  '10',  '7',  '9',  '6',  '9',  '4',  '5',  '2',  '10',  '6',  '6',  '1',  '7',  '8',  '2',  '4',  '6',  '3',  '10',  '2',  '9',  '8',  '5',  '1',  '3',  '8',  '3',  '4',  '7',  '4',  '1',  '5',  '8',  '9',  '1',  '7',  '2',  '5']
        item_ids = ['Item6',  'Item1',  'Item9',  'Item2',  'Item10',  'Item3',  'Item4',  'Item4',  'Item2',  'Item4',  'Item10',  'Item1',  'Item3',  'Item5',  'Item5',  'Item2',  'Item7',  'Item5',  'Item6',  'Item10',  'Item2',  'Item3',  'Item9',  'Item10',  'Item5',  'Item6',  'Item8',  'Item8',  'Item7',  'Item4',  'Item1',  'Item1',  'Item8',  'Item8',  'Item9',  'Item7',  'Item9',  'Item3',  'Item6',  'Item7']
        prod_ids = ['Prod4',  'Prod2',  'Prod4',  'Prod1',  'Prod5',  'Prod3',  'Prod1',  'Prod3',  'Prod1',  'Prod5',  'Prod3',  'Prod4',  'Prod3',  'Prod3',  'Prod4',  'Prod3',  'Prod4',  'Prod5',  'Prod2',  'Prod2',  'Prod1',  'Prod3',  'Prod5',  'Prod4',  'Prod2',  'Prod1',  'Prod1',  'Prod3',  'Prod5',  'Prod5',  'Prod4',  'Prod2',  'Prod2',  'Prod5',  'Prod1',  'Prod5',  'Prod2',  'Prod4',  'Prod1',  'Prod2']
        net_untis = [6,  8,  7,  2,  6,  4,  2,  5,  10,  8,  8,  10,  3,  6,  5,  5,  6,  10,  3,  2,  1,  7,  3,  9,  5,  9,  9,  1,  4,  1,  8,  4,  1,  3,  2,  7,  9,  10,  7,  4]
        net_amnt = [1,  1,  4,  10,  2,  2,  7,  1,  4,  5,  4,  3,  1,  8,  2,  9,  6,  6,  4,  9,  10,  2,  3,  9,  5,  5,  9,  10,  7,  7,  8,  3,  6,  6,  7,  5,  8,  8,  10,  3]
        YearMonth = [202202,  202205,  202203,  202202,  202208,  202207,  202209,  202211,  202203,  202207,  202206,  202205,  202302,  202204,  202210,  202207,  202208,  202208,  202211,  202206,  202210,  202204,  202212,  202206,  202302,  202201,  202209,  202210,  202301,  202301,  202209,  202201,  202202,  202211,  202205,  202212,  202204,  202201,  202212,  202203]

        sales_data = {
            'NARC': customer_ids,
            'YearMonth': YearMonth,
            'ProdID': prod_ids,
            'ItemID': item_ids,
            'Units': net_untis,
            'Sales': net_amnt
        }

        alignment_data = {
            'NARC': ['1', '1', '1', '1', '1', '1', '2', '2', '2', '2', '2', '2', '3', '3', '3', '3', '3', '3', '4', '4', '4', '4', '4', '4', '5', '5', '5', '5', '5', '5', '6', '6', '6', '6', '6', '6', '7', '7', '7', '7', '7', '7', '8', '8', '8', '8', '8', '8', '9', '9', '9', '9', '9', '9', '10', '10', '10', '10', '10', '10'],
            'SalesForce_ID': ['100', '101', '104', '752', '759', '760', '100', '101', '104', '752', '759', '760', '100', '101', '104', '752', '759', '760', '100', '101', '104', '752', '759', '760', '100', '101', '104', '752', '759', '760', '100', '101', '104', '752', '759', '760', '100', '101', '104', '752', '759', '760', '100', '101', '104', '752', '759', '760', '100', '101', '104', '752', '759', '760', '100', '101', '104', '752', '759', '760'],
            'Region_ID': [
                'None', 'None', 'CST_A', 'None', 'EA_A', 'CST_IDSR_A', 
                'None', 'None', 'CST_B', 'None', 'None', 'CST_IDSR_B', 
                'None', 'None', 'CST_C', 'None', 'EA_C', 'CST_IDSR_C', 
                'None', 'None', 'CST_A', 'None', 'EA_A', 'CST_IDSR_A', 
                'Rx100_1', 'Rx101_1', 'None', 'Rx_IDSR_1', 'EA_A', 'None', 
                'None', 'Rx_101_1', 'CST_A', 'None', 'None', 'CST_IDSR_B',
                'None', 'Rx_101_1', 'CST_B', 'None', 'None', 'CST_IDSR_A',
                'None', 'None', 'CST_B', 'None', 'None', 'CST_IDSR_B',
                'Rx100_1', 'None', 'None', 'Rx_IDSR_1', 'None', 'None',
                'None', 'Rx_101_1', 'CST_C', 'None', 'None', 'CST_IDSR_C'
            ],
            'Region_Name': [
                'None_Name', 'None_Name', 'CST_A_Name', 'None_Name', 'EA_A_Name', 'CST_IDSR_A_Name',
                'None_Name', 'None_Name', 'CST_B_Name', 'None_Name', 'None_Name', 'CST_IDSR_B_Name',
                'None_Name', 'None_Name', 'CST_C_Name', 'None_Name', 'EA_C_Name', 'CST_IDSR_C_Name',
                'None_Name', 'None_Name', 'CST_A_Name', 'None_Name', 'EA_A_Name', 'CST_IDSR_A_Name',
                'Rx100_1_Name', 'Rx101_1_Name', 'None_Name', 'Rx_IDSR_1_Name', 'EA_A_Name', 'None_Name',
                'None_Name', 'Rx_101_1_Name', 'CST_A_Name', 'None_Name', 'None_Name', 'CST_IDSR_B_Name',
                'None_Name', 'Rx_101_1_Name', 'CST_B_Name', 'None_Name', 'None_Name', 'CST_IDSR_A_Name',
                'None_Name', 'None_Name', 'CST_B_Name', 'None_Name', 'None_Name', 'CST_IDSR_B_Name',
                'Rx100_1_Name', 'None_Name', 'None_Name', 'Rx_IDSR_1_Name', 'None_Name', 'None_Name',
                'None_Name', 'Rx_101_1_Name', 'CST_C_Name', 'None_Name', 'None_Name', 'CST_IDSR_C_Name'
            ],
            'Region_Manager': [
                'None_Manager', 'None_Manager', 'CST_A_Manager', 'None_Manager', 'EA_A_Manager', 'CST_IDSR_A_Manager',
                'None_Manager', 'None_Manager', 'CST_B_Manager', 'None_Manager', 'None_Manager', 'CST_IDSR_B_Manager',
                'None_Manager', 'None_Manager', 'CST_C_Manager', 'None_Manager', 'EA_C_Manager', 'CST_IDSR_C_Manager',
                'None_Manager', 'None_Manager', 'CST_A_Manager', 'None_Manager', 'EA_A_Manager', 'CST_IDSR_A_Manager',
                'Rx100_1_Manager', 'Rx101_1_Manager', 'None_Manager', 'Rx_IDSR_1_Manager', 'EA_A_Manager', 'None_Manager',
                'None_Manager', 'Rx_101_1_Manager', 'CST_A_Manager', 'None_Manager', 'None_Manager', 'CST_IDSR_B_Manager',
                'None_Manager', 'Rx_101_1_Manager', 'CST_B_Manager', 'None_Manager', 'None_Manager', 'CST_IDSR_A_Manager',
                'None_Manager', 'None_Manager', 'CST_B_Manager', 'None_Manager', 'None_Manager', 'CST_IDSR_B_Manager',
                'Rx100_1_Manager', 'None_Manager', 'None_Manager', 'Rx_IDSR_1_Manager', 'None_Manager', 'None_Manager',
                'None_Manager', 'Rx_101_1_Manager', 'CST_C_Manager', 'None_Manager', 'None_Manager', 'CST_IDSR_C_Manager'
            ],
            'Area_ID': [
                'None_A_ID', 'None_A_ID', 'CST_A_A_ID', 'None_A_ID', 'EA_A_A_ID', 'CST_IDSR_A_A_ID',
                'None_A_ID', 'None_A_ID', 'CST_B_A_ID', 'None_A_ID', 'None_A_ID', 'CST_IDSR_B_A_ID',
                'None_A_ID', 'None_A_ID', 'CST_C_A_ID', 'None_A_ID', 'EA_C_A_ID', 'CST_IDSR_C_A_ID',
                'None_A_ID', 'None_A_ID', 'CST_A_A_ID', 'None_A_ID', 'EA_A_A_ID', 'CST_IDSR_A_A_ID',
                'Rx100_1_A_ID', 'Rx101_1_A_ID', 'None_A_ID', 'Rx_IDSR_1_A_ID', 'EA_A_A_ID', 'None_A_ID',
                'None_A_ID', 'Rx_101_1_A_ID', 'CST_A_A_ID', 'None_A_ID', 'None_A_ID', 'CST_IDSR_B_A_ID',
                'None_A_ID', 'Rx_101_1_A_ID', 'CST_B_A_ID', 'None_A_ID', 'None_A_ID', 'CST_IDSR_A_A_ID',
                'None_A_ID', 'None_A_ID', 'CST_B_A_ID', 'None_A_ID', 'None_A_ID', 'CST_IDSR_B_A_ID',
                'Rx100_1_A_ID', 'None_A_ID', 'None_A_ID', 'Rx_IDSR_1_A_ID', 'None_A_ID', 'None_A_ID',
                'None_A_ID', 'Rx_101_1_A_ID', 'CST_C_A_ID', 'None_A_ID', 'None_A_ID', 'CST_IDSR_C_A_ID'
            ],
            'Area_Name': [
                'None_A_Name', 'None_A_Name', 'CST_A_A_Name', 'None_A_Name', 'EA_A_A_Name', 'CST_IDSR_A_A_Name',
                'None_A_Name', 'None_A_Name', 'CST_B_A_Name', 'None_A_Name', 'None_A_Name', 'CST_IDSR_B_A_Name',
                'None_A_Name', 'None_A_Name', 'CST_C_A_Name', 'None_A_Name', 'EA_C_A_Name', 'CST_IDSR_C_A_Name',
                'None_A_Name', 'None_A_Name', 'CST_A_A_Name', 'None_A_Name', 'EA_A_A_Name', 'CST_IDSR_A_A_Name',
                'Rx100_1_A_Name', 'Rx101_1_A_Name', 'None_A_Name', 'Rx_IDSR_1_A_Name', 'EA_A_A_Name', 'None_A_Name',
                'None_A_Name', 'Rx_101_1_A_Name', 'CST_A_A_Name', 'None_A_Name', 'None_A_Name', 'CST_IDSR_B_A_Name',
                'None_A_Name', 'Rx_101_1_A_Name', 'CST_B_A_Name', 'None_A_Name', 'None_A_Name', 'CST_IDSR_A_A_Name',
                'None_A_Name', 'None_A_Name', 'CST_B_A_Name', 'None_A_Name', 'None_A_Name', 'CST_IDSR_B_A_Name',
                'Rx100_1_A_Name', 'None_A_Name', 'None_A_Name', 'Rx_IDSR_1_A_Name', 'None_A_Name', 'None_A_Name',
                'None_A_Name', 'Rx_101_1_A_Name', 'CST_C_A_Name', 'None_A_Name', 'None_A_Name', 'CST_IDSR_C_A_Name'
            ],
            'Area_Manager': [
                'None_A_Manager', 'None_A_Manager', 'CST_A_A_Manager', 'None_A_Manager', 'EA_A_A_Manager', 'CST_IDSR_A_A_Manager',
                'None_A_Manager', 'None_A_Manager', 'CST_B_A_Manager', 'None_A_Manager', 'None_A_Manager', 'CST_IDSR_B_A_Manager',
                'None_A_Manager', 'None_A_Manager', 'CST_C_A_Manager', 'None_A_Manager', 'EA_C_A_Manager', 'CST_IDSR_C_A_Manager',
                'None_A_Manager', 'None_A_Manager', 'CST_A_A_Manager', 'None_A_Manager', 'EA_A_A_Manager', 'CST_IDSR_A_A_Manager',
                'Rx100_1_A_Manager', 'Rx101_1_A_Manager', 'None_A_Manager', 'Rx_IDSR_1_A_Manager', 'EA_A_A_Manager', 'None_A_Manager',
                'None_A_Manager', 'Rx_101_1_A_Manager', 'CST_A_A_Manager', 'None_A_Manager', 'None_A_Manager', 'CST_IDSR_B_A_Manager',
                'None_A_Manager', 'Rx_101_1_A_Manager', 'CST_B_A_Manager', 'None_A_Manager', 'None_A_Manager', 'CST_IDSR_A_A_Manager',
                'None_A_Manager', 'None_A_Manager', 'CST_B_A_Manager', 'None_A_Manager', 'None_A_Manager', 'CST_IDSR_B_A_Manager',
                'Rx100_1_A_Manager', 'None_A_Manager', 'None_A_Manager', 'Rx_IDSR_1_A_Manager', 'None_A_Manager', 'None_A_Manager',
                'None_A_Manager', 'Rx_101_1_A_Manager', 'CST_C_A_Manager', 'None_A_Manager', 'None_A_Manager', 'CST_IDSR_C_A_Manager'
            ],
            'Territory_ID': [
                'None_T_ID', 'None_T_ID', 'CST_A_T_ID', 'None_T_ID', 'EA_A_T_ID', 'CST_IDSR_A_T_ID',
                'None_T_ID', 'None_T_ID', 'CST_B_T_ID', 'None_T_ID', 'None_T_ID', 'CST_IDSR_B_T_ID',
                'None_T_ID', 'None_T_ID', 'CST_C_T_ID', 'None_T_ID', 'EA_C_T_ID', 'CST_IDSR_C_T_ID',
                'None_T_ID', 'None_T_ID', 'CST_A_T_ID', 'None_T_ID', 'EA_A_T_ID', 'CST_IDSR_A_T_ID',
                'Rx100_1_T_ID', 'Rx101_1_T_ID', 'None_T_ID', 'Rx_IDSR_1_T_ID', 'EA_A_T_ID', 'None_T_ID',
                'None_T_ID', 'Rx_101_1_T_ID', 'CST_A_T_ID', 'None_T_ID', 'None_T_ID', 'CST_IDSR_B_T_ID',
                'None_T_ID', 'Rx_101_1_T_ID', 'CST_B_T_ID', 'None_T_ID', 'None_T_ID', 'CST_IDSR_A_T_ID',
                'None_T_ID', 'None_T_ID', 'CST_B_T_ID', 'None_T_ID', 'None_T_ID', 'CST_IDSR_B_T_ID',
                'Rx100_1_T_ID', 'None_T_ID', 'None_T_ID', 'Rx_IDSR_1_T_ID', 'None_T_ID', 'None_T_ID',
                'None_T_ID', 'Rx_101_1_T_ID', 'CST_C_T_ID', 'None_T_ID', 'None_T_ID', 'CST_IDSR_C_T_ID'
            ],
            'Territory_Name': [
                'None_T_Name', 'None_T_Name', 'CST_A_T_Name', 'None_T_Name', 'EA_A_T_Name', 'CST_IDSR_A_T_Name',
                'None_T_Name', 'None_T_Name', 'CST_B_T_Name', 'None_T_Name', 'None_T_Name', 'CST_IDSR_B_T_Name',
                'None_T_Name', 'None_T_Name', 'CST_C_T_Name', 'None_T_Name', 'EA_C_T_Name', 'CST_IDSR_C_T_Name',
                'None_T_Name', 'None_T_Name', 'CST_A_T_Name', 'None_T_Name', 'EA_A_T_Name', 'CST_IDSR_A_T_Name',
                'Rx100_1_T_Name', 'Rx101_1_T_Name', 'None_T_Name', 'Rx_IDSR_1_T_Name', 'EA_A_T_Name', 'None_T_Name',
                'None_T_Name', 'Rx_101_1_T_Name', 'CST_A_T_Name', 'None_T_Name', 'None_T_Name', 'CST_IDSR_B_T_Name',
                'None_T_Name', 'Rx_101_1_T_Name', 'CST_B_T_Name', 'None_T_Name', 'None_T_Name', 'CST_IDSR_A_T_Name',
                'None_T_Name', 'None_T_Name', 'CST_B_T_Name', 'None_T_Name', 'None_T_Name', 'CST_IDSR_B_T_Name',
                'Rx100_1_T_Name', 'None_T_Name', 'None_T_Name', 'Rx_IDSR_1_T_Name', 'None_T_Name', 'None_T_Name',
                'None_T_Name', 'Rx_101_1_T_Name', 'CST_C_T_Name', 'None_T_Name', 'None_T_Name', 'CST_IDSR_C_T_Name'
            ],
            'Territory_Manager': [
                'None_T_Manager', 'None_T_Manager', 'CST_A_T_Manager', 'None_T_Manager', 'EA_A_T_Manager', 'CST_IDSR_A_T_Manager',
                'None_T_Manager', 'None_T_Manager', 'CST_B_T_Manager', 'None_T_Manager', 'None_T_Manager', 'CST_IDSR_B_T_Manager',
                'None_T_Manager', 'None_T_Manager', 'CST_C_T_Manager', 'None_T_Manager', 'EA_C_T_Manager', 'CST_IDSR_C_T_Manager',
                'None_T_Manager', 'None_T_Manager', 'CST_A_T_Manager', 'None_T_Manager', 'EA_A_T_Manager', 'CST_IDSR_A_T_Manager',
                'Rx100_1_T_Manager', 'Rx101_1_T_Manager', 'None_T_Manager', 'Rx_IDSR_1_T_Manager', 'EA_A_T_Manager', 'None_T_Manager',
                'None_T_Manager', 'Rx_101_1_T_Manager', 'CST_A_T_Manager', 'None_T_Manager', 'None_T_Manager', 'CST_IDSR_B_T_Manager',
                'None_T_Manager', 'Rx_101_1_T_Manager', 'CST_B_T_Manager', 'None_T_Manager', 'None_T_Manager', 'CST_IDSR_A_T_Manager',
                'None_T_Manager', 'None_T_Manager', 'CST_B_T_Manager', 'None_T_Manager', 'None_T_Manager', 'CST_IDSR_B_T_Manager',
                'Rx100_1_T_Manager', 'None_T_Manager', 'None_T_Manager', 'Rx_IDSR_1_T_Manager', 'None_T_Manager', 'None_T_Manager',
                'None_T_Manager', 'Rx_101_1_T_Manager', 'CST_C_T_Manager', 'None_T_Manager', 'None_T_Manager', 'CST_IDSR_C_T_Manager'
            ]
        }

        self.customers = pd.DataFrame(customer_data)
        self.sales = pd.DataFrame(sales_data)
        self.alignments = pd.DataFrame(alignment_data)
