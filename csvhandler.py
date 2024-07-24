import pandas 

class CsvHandler():
     
      def ReadContentOfCsv() -> pandas.DataFrame:
            data = pandas.read_csv("50_states.csv") 
            return data
      
    
      def CheckInput(self,input:str) -> tuple:
            data = CsvHandler.ReadContentOfCsv()

            states_list = data.state.to_list()
            if (input in states_list):
                 coordinates = CsvHandler.GetCoordinatesOfState(input,data)
                 return coordinates
            else:
                 return (0,0)

      def GetCoordinatesOfState(state_name:str,data:pandas.DataFrame) -> tuple:
          state_row = data[data["state"]==state_name]
          new_x = state_row.iloc[0]['x']
          new_y = state_row.iloc[0]['y']
          coordinates = (new_x,new_y)
          return coordinates
            
            
                 