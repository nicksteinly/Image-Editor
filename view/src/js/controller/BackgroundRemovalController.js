
export class BackgroundRemovalController{
  constructor(baseURL) {
    this.baseURL = baseURL;
  }

  async removeBlackBackground({ inputImagePath }) {
    try {
      const response = await fetch(`${this.baseURL}/remove_black_background`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        withCredentials: true,
        body: JSON.stringify({ inputImagePath: inputImagePath }),
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