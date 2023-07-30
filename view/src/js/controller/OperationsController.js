
export class OperationsController{
  constructor(baseURL){
    this.baseURL = baseURL
  }

  async getOperations(){
    try{
      const response = await fetch(`${this.baseURL}/get_operations`, {
        method: 'GET',
        headers: {
          'Content-Type': 'application/json',
        },
        withCredentials: true,
      });
      if (!response.ok) {
        throw new Error('Failed to fetch data');
      }
      const operations = await response.json();
      return operations?.operations;
     } catch (error) {
        console.error('Error:', error);
        throw error; 
    }
  }

  async retrieveOperationNames(){
    try{
      const response = await fetch(`${this.baseURL}/retrieve_operation_names`, {
        method: 'GET',
        headers: {
          'Content-Type': 'application/json',
        },
        withCredentials: true,
      });
        
      if (!response.ok) {
        throw new Error('Failed to fetch data');
      }

      const operations = await response.json();
      return operations.names;
    } catch (error) {
      console.error('Error:', error);
      throw error; 
    }
  }

  async retrieveOperationParameters(operationName){
    try{
      const response = await fetch(`${this.baseURL}/retrieve_operation_parameters`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        withCredentials: true,
        body: JSON.stringify({operationName: operationName}),
      });
        
      if (!response.ok) {
        throw new Error('Failed to fetch data');
      }

      const data = await response.json();
      return data.parameters;
    } catch (error) {
      console.error('Error:', error);
      throw error; 
    }
  }

  async retrieveOperationDescription(operationName){
    try{
      const response = await fetch(`${this.baseURL}/retrieve_operation_description`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        withCredentials: true,
        body: JSON.stringify({operationName: operationName}),
      });
        
      if (!response.ok) {
        throw new Error('Failed to fetch data');
      }

      const data = await response.json();
      return data.description;
    } catch (error) {
      console.error('Error:', error);
      throw error; 
    }
  }

  async submitOperations(operationsJSON){
    try{
      const response = await fetch(`${this.baseURL}/call_operations`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        withCredentials: true,
        body: JSON.stringify({'operations': [operationsJSON]}),
      });
      console.log(operationsJSON);
      if (!response.ok) {
        throw new Error('Failed to fetch data');
      }

      const data = await response.json();
      return data;
    } catch (error) {
      console.error('Error:', error);
      throw error; 
    }
  }

}