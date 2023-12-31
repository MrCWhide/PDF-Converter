# PDF-Converter
# Python PDF转换器项目

本项目旨在使用Python编写一个PDF转换器，通过使用 `pdf2docx` 库实现将PDF文件转换为DOCX文件的功能。

## 功能特点

- **PDF到DOCX转换**：利用 `pdf2docx` 库实现高效的PDF文件转换成DOCX格式文件。
- **简单易用**：提供简单的命令行接口，后续继续编写gui界面，使用户可以轻松使用该转换器。
- **扩展性**：可根据需求扩展其他格式转换功能或添加额外的功能特性。

## 技术栈

- **Python**：使用Python3作为主要编程语言。
- **pdf2docx库**：利用该库进行PDF到DOCX的转换操作。
- **封装**：通过python-pyinstaller封装

## 使用示例
### 方法1：在目录下放入test.pdf后运行main.py
### 方法2：运行dist目录里的可执行文件（也可以下载release里的可执行文件），确保可执行文件同目录下有test.pdf