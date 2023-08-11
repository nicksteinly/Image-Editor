
export class CoinsController{
  constructor() {
    this.baseURL = "http://127.0.0.1:5000/object-detection/template-matching/coins";
  }

  async labelCoinsExample() {
    try {
      const response = await fetch(`${this.baseURL}/label_coins`, {
        method: 'GET',
        headers: {
          'Content-Type': 'application/json',
        },
        withCredentials: true,
      });

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