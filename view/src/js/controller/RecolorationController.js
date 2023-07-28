
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

}