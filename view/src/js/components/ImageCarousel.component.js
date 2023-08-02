import React from 'react';
import Slider from 'react-slick';
import '../../css/image-carousel.css';
import 'slick-carousel/slick/slick.css';
import 'slick-carousel/slick/slick-theme.css';
import 'bootstrap/dist/css/bootstrap.min.css';
import { useOperation } from '../context/OperationProvider';

// Import Bootstrap icons for previous and next arrows
import { BsChevronLeft, BsChevronRight } from 'react-icons/bs';

export const ImageCarousel = () => {
  const imagesData = useOperation().imagesData;
  
  // Custom arrow components for previous and next navigation
  const PrevArrow = (props) => {
    const { onClick } = props;
    return (
      <div className="slick-arrow custom-prev-arrow" onClick={onClick}>
        <BsChevronLeft />
      </div>
    );
  };

  const NextArrow = (props) => {
    const { onClick } = props;
    return (
      <div className="slick-arrow custom-next-arrow" onClick={onClick}>
        <BsChevronRight />
      </div>
    );
  };

  const settings = {
    dots: true,
    infinite: true,
    speed: 500,
    slidesToShow: 1,
    slidesToScroll: 1,
    prevArrow: <PrevArrow />, // Use the custom previous arrow component
    nextArrow: <NextArrow />, // Use the custom next arrow component
  };

  return (
    <div id="image-carousel-container">
      <div id="image-carousel">
        <Slider {...settings}>
        {imagesData &&
          imagesData.map((imageData, index) => (
            <img
              src={`data:image/png;base64,${imageData}`}
              alt="Your Image"
              width={'50%'}
              height={'50%'}
              key={index}
            />
          ))}
      </Slider>
      </div>
    </div>
  );
};
