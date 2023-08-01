import React from 'react';
import Slider from 'react-slick';
import 'slick-carousel/slick/slick.css';

export const ImageCarousel = ({ imagesData }) => {
  const settings = {
    dots: true,
    infinite: true,
    speed: 500,
    slidesToShow: 1,
    slidesToScroll: 1,
  };

  return (
    <Slider {...settings}>
      {imagesData &&
        imagesData.map((imageData, index) => (
          <img src={`data:image/png;base64,${imageData}`} alt="Your Image" width={'50%'} height={'50%'} key={index}/>
        ))}
    </Slider>
  );
};
