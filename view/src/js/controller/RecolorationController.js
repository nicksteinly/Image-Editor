
export class RecolorationController{
  constructor(baseURL){
    this.baseURL = baseURL
  }

  async recolor_white_pixels({inputImagePath, color}) {
    try {
      const response = await fetch(`${this.baseURL}/recolor_white_pixels`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        withCredentials: true,
        body: JSON.stringify({ inputImagePath: inputImagePath, hexColor: color }),
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

  async filter_out_color({inputImagePath, targetColor, threshold}) {
    try {
      const response = await fetch(`${this.baseURL}/filter_out_color`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        withCredentials: true,
        body: JSON.stringify({ inputImagePath: inputImagePath, targetColor: targetColor, threshold: threshold }),
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

  async filter_by_color({inputImagePath, targetColor, threshold}) {
    try {
      const response = await fetch(`${this.baseURL}/filter_by_color`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        withCredentials: true,
        body: JSON.stringify({ inputImagePath: inputImagePath, targetColor: targetColor, threshold: threshold }),
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