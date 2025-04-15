import cv2
import pytesseract
from diffusers import StableDiffusionPipeline
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
import numpy as np
from stegano import lsb
import os
