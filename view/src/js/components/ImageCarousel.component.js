import React, { useRef } from 'react';
import '../../css/image-carousel.css'

export const ImageCarousel = ({ imagesData }) => {
  const carouselRef = useRef(null);

  const handleNext = () => {
    if (carouselRef.current) {
      carouselRef.current.scrollBy({
        top: 0,
        left: carouselRef.current.offsetWidth,
        behavior: 'smooth',
      });
    }
  };

  const handlePrev = () => {
    if (carouselRef.current) {
      carouselRef.current.scrollBy({
        top: 0,
        left: -carouselRef.current.offsetWidth,
        behavior: 'smooth',
      });
    }
  };

  return (
    <div className="carousel-container">
      <div className="carousel" ref={carouselRef}>
        {imagesData &&
          imagesData.map((imageData, index) => (
            <div key={index} className="carousel-item">
              <img
                src={`data:image/png;base64,${imageData}`}
                alt="Your Image"
                width={'50%'}
                height={'50%'}
              />
            </div>
          ))}
      </div>
      <button className="prev-button" onClick={handlePrev}>
        previous
      </button>
      <button className="next-button" onClick={handleNext}>
        next
      </button>
    </div>
  );
};
