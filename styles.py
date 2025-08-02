#!/usr/bin/env python
# coding: utf-8

styles  = """
<style>

.title {
  width: 100%;
  margin: 0 auto 25px auto;
  padding: 20px 10px;
  background-color: #0A0F2C;
  color: #4AC4FF;
  font-weight: bold;
  font-family: 'Century Gothic', sans-serif;
  font-size: clamp(16px, 3vw, 20px);
  text-align: center;
  border-radius: 25px;
  box-shadow: 0 4px 12px rgba(74, 196, 255, 0.25);
}

/* === کانتینر معرفی === */
.about-container {
  max-width: 600px;
  margin: 40px auto;
  padding: 25px 30px;
  border: 2px solid #8B4D9C;
  border-radius: 20px;
  background: linear-gradient(145deg, #E5E7EB, #D176C4);
  box-shadow: 0 8px 20px rgba(138, 43, 226, 0.15);
  text-align: center;
  font-family: 'Century Gothic', sans-serif;
  color: #0A0F2C;
}
.about-container p {
  font-size: 16px;
  line-height: 1.6;
}
.about-container b {
  font-size: 18px;
}

/* === دکمه‌ها (fancy-button) === */
.fancy-button {
  display: inline-flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  width: 130px;
  height: 55px;
  margin: 8px;
  background-color: transparent;
  color: #FFA500;
  border: 2px solid #FFA500;
  border-radius: 25px;
  text-align: center;
  text-decoration: none !important;
  font-size: 13px;
  font-weight: bold;
  font-family: 'Century Gothic', sans-serif;
  transition: all 0.3s ease;
}
.fancy-button:hover {
  background-color: #FFA500;
  color: #0A0F2C !important;
  transform: scale(1.05);
  text-decoration: none !important;
}
.button-row {
  display: flex;
  justify-content: center;
  gap: 10px;
  flex-wrap: wrap;
  margin-top: 20px;
}

/* === Table Of Contents === */
.text-container {
  text-align: center;
  font-size: 12px;
  margin: 5px;
  padding: 5px;
}
.text {
  display: inline-block;
  padding: 20px 60px; 
  border-top-left-radius: 60px;
  border-top-right-radius: 30px;
  border-bottom-right-radius: 60px;
  border-bottom-left-radius: 30px;
  background-color: #4AC4FF;
  color: #0A0F2C;
  font-weight: bold;
  font-size: 22px; 
  font-family: 'Century Gothic';
  width: auto;
  text-align: center;
}

/* === TOC Buttons === */
.button {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 600px;
  height: 60px;
  margin: 10px auto;
  background-color: #8B4D9C;
  color: #F8F1FF;
  border: none;
  border-radius: 50px;
  text-align: center;
  text-decoration: none;
  font-size: 18px;
  font-weight: 600;
  font-family: 'Century Gothic';
  transition: transform 0.6s ease, background-position 0s ease, color 0.3s ease;
}
.button:hover {
  background-image: linear-gradient(to right, #D176C4 0%, #8B4D9C 50%, #D176C4 100%);
  background-size: 300% 100%;
  background-position: 100% 0%;
  transform: scale(1.1);
  color: #FFA500;
}

/* === Responsive (Mobile) === */
@media (max-width: 500px) {
  .fancy-button {
    width: 90%;
    font-size: 14px;
  }
  .button-row {
    flex-direction: column;
    align-items: center;
  }
  .button {
    width: 90%;
  }
}

</style>
"""
