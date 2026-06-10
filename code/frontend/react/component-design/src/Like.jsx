import React, { useState } from 'react';
import './LikeButton.css';

export default function LikeButton() {
  const [liked, setLiked] = useState(false);
  const [animate, setAnimate] = useState(false);

  const handleLikeClick = () => {
    setLiked(!liked);
    // Trigger pop animation only when liking
    if (!liked) {
      setAnimate(true);
      setTimeout(() => setAnimate(false), 300);
    }
  };

  return (
    <div className="card-action-container">
      <button 
        className={`like-button ${liked ? 'is-liked' : ''} ${animate ? 'animate-pop' : ''}`}
        onClick={handleLikeClick}
        aria-label={liked ? "Unlike post" : "Like post"}
      >
        <svg 
          viewBox="0 0 24 24" 
          width="24" 
          height="24" 
          className="heart-icon"
        >
          <path d="M12 21.35l-1.45-1.32C5.4 15.36 2 12.28 2 8.5 2 5.42 4.42 3 7.5 3c1.74 0 3.41.81 4.5 2.09C13.09 3.81 14.76 3 16.5 3 19.58 3 22 5.42 22 8.5c0 3.78-3.4 6.86-8.55 11.54L12 21.35z" />
        </svg>
      </button>
    </div>
  );
}
