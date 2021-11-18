From python:3
ADD my_script.py /
RUN pip install fastapi
RUN pip install pydantic
RUN pip install typing
CMD ["python", "./my_script.py"]
