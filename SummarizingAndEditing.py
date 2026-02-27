import os
from xmlrpc import client
from dotenv import load_dotenv
from openai import OpenAI
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError("OPENAI_API_KEY not found in env file")

#Find and replace

prompt="""Replace car with plane and adjust phrase:
A car is a vehicle that is typically powered by an internal combustion engine or an electric motor. It has four wheels, and is designed to carry passengers and/or cargo on roads or highways. Cars have become a ubiquitous part of modern society, and are used for a wide variety of purposes, such as commuting, travel, and transportation of goods. Cars are often associated with freedom, independence, and mobility."""

def get_response(prompt):
    client = OpenAI(api_key = api_key)
    response = client.chat.completions.create(
        model="gpt-4o-mini", max_completion_tokens=100,
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content

findAndReplace = get_response(prompt)
print(findAndReplace)

#Text summarization

finance_text = """
Finance is the study of managing money, focusing on how individuals, companies, and governments acquire, spend, and invest funds. Key areas include corporate finance, investment management, and personal finance, focusing on assets, liabilities, and risk. Core concepts include net present value (NPV), cash flow analysis, and capital structure. 
Here is a breakdown of key finance concepts and terminology:
Financial Statements: Essential reports including the income statement, balance sheet, and cash flow statement, which track a company's financial health.
Assets and Liabilities: Assets are resources with economic value (e.g., cash, property), while liabilities are obligations, such as loans and debts.
Investment Basics: The allocation of money with expectations of profit, involving stocks, bonds, or real assets.
Core Principles: Successful financial management relies on budgeting, saving, understanding credit, and managing risk.
Key Financial Metrics:
Return on Investment (ROI): A measure used to evaluate the efficiency of an investment.
Net Present Value (NPV): A method to determine the value of an investment by calculating the present value of future cash flows.
Equity: The value of shares issued by a company or the value of an asset after deducting liabilities. 
For foundational knowledge, texts like Benjamin Graham's "The Intelligent Investor" emphasize value-oriented investing, while Morgan Housel's "The Psychology of Money" focuses on the emotional aspects of wealth management. 
"""

prompt = f"""Summarize the following text into two concise bullet points:
{finance_text}"""

def summarize_text(prompt):
    client = OpenAI(api_key = api_key)
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        max_completion_tokens=400
    )
    return response.choices[0].message.content

response_summary = summarize_text(prompt)
print(response_summary)