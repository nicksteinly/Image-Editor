import React, { useState, useEffect } from "react";
import { HeaderComponent } from "../components/Header.component";
import { CoinsController } from "../controller/computer_vision/object_detection/template_matching/CoinsController";

export const TemplateMatchingPage = () => {
  const coinsController = new CoinsController();
  const [data, setData] = useState(null);

  useEffect(() => {
    const fetchData = async () => {
      const result = await coinsController.labelCoinsExample();
      setData(result);
    };

    fetchData();
  }, []);

  return (
    <div>
      <HeaderComponent header={"Template Matching"} />
      <ul>
        <li>
          Example/Notes
        </li>
        <li>
          Analyze Image
        </li>
      </ul>
      <p>
        Template matching is a technique for finding areas of an image that are
        similar to a patch (template). A patch is a small image with certain
        features. The goal of template matching is to find the patch/template in
        an image.
      </p>
      {data && (
        <div>
          {console.log(data?.plots.map((imageData) => imageData))}
          {/* Render your plots here */}
          {data?.plots.map((imageData, index) => (
            <img
              src={`data:image/png;base64,${imageData}`}
              alt="Your Image"
              width={'50%'}
              height={'50%'}
              key={index}
            />
          ))}
          <p>Total Value: {data.total_value}</p>
          <p>Coin Count: 
            {console.log(data.coin_count)}
            {Object.entries(data.coin_count).map(([key, value]) => (
              <p>{key}: {value}</p>
            ))}
          </p>
        </div>
      )}
    </div>
  );
};
