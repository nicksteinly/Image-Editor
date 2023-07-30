import React, { useState } from 'react';

const ImageCarousel = ({ images }) => {
  const [currentImageIndex, setCurrentImageIndex] = useState(0);

  const goToNextImage = () => {
    setCurrentImageIndex((prevIndex) => (prevIndex + 1) % images.length);
  };

  const goToPrevImage = () => {
    setCurrentImageIndex((prevIndex) => (prevIndex - 1 + images.length) % images.length);
  };

  return (
    <div className="image-carousel">
      <div className="image-container">
        <img src={images[currentImageIndex]} alt={`Image ${currentImageIndex}`} />
      </div>
      <div className="controls">
        <button onClick={goToPrevImage}>Previous</button>
        <button onClick={goToNextImage}>Next</button>
      </div>
    </div>
  );
};

export default ImageCarousel;
