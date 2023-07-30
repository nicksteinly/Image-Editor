
export class EdgeDetectionController{
  constructor(baseURL){
    this.baseURL = baseURL
  }

  // using a combination of await and .then() to handle the response, which can lead to unexpected behavior.
  // so dont use .then() and instead use await like below
  async cannyDetection({inputImagePath}) {
    try {
      const response = await fetch(`${this.baseURL}/edge_detection_Canny`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        withCredentials: true,
        body: JSON.stringify({ imagePath: inputImagePath }), 
      });
  
      if (!response.ok) {
        throw new Error('Failed to fetch data');
      }
  
      const data = await response.json();
      return data.outputImagePath;

    } catch (error) {
      console.error('Error:', error);
      throw error; 
    }
  }

  async outerOutlineDetection({inputImagePath}){
    try{
      const response = await fetch(`${this.baseURL}/outer_outline_detection`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        withCredentials: true,
        body: JSON.stringify({ imagePath: inputImagePath }),
      });
        
      if (!response.ok) {
        throw new Error('Failed to fetch data');
      }

      const data = await response.json();
      return data.outputImagePath;

    } catch (error) {
      console.error('Error:', error);
      throw error; 
    }
  }

  async thickenEdges({ inputImagePath, kernelSize, iterations }) {
    try {
      const response = await fetch(`${this.baseURL}/thickened_edges`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        withCredentials: true,
        body: JSON.stringify({ imagePath: inputImagePath, kernelSize, iterations }), 
      });
  
      if (!response.ok) {
        throw new Error('Failed to fetch data');
      }
  
      const data = await response.json();
      return data.outputImage;
    } catch (error) {
      console.error('Error:', error);
      throw error;
    }
  }

}