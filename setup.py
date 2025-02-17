from setuptools import setup, find_packages

setup(
    name="trade",
    version="0.1",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "t=trade.trade_console:main",
            "trade=trade.trade_detailed_console:main",
        ],
    },
    install_requires=[],
    description="Trading price calculator CLI tool",
    author="Imran Pollob",
    author_email="polboy777@gmail.com",
)
