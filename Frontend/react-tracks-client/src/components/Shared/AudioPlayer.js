import React from "react";
import ReactPlayer from "react-player";

const AudioPlayer = ({ url }) => (
  <div>
    <ReactPlayer url={url} height="30px" width="500px" controls={true} />
  </div>
);

export default AudioPlayer;