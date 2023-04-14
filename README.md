# GIC IAP Application

This is an assessment of Zhang Cheng Chuan for GIC's IAP application.

## Table of Contents

- [Installation and Usage](#installation-and-usage)
- [Design](#design)
- [Assumptions](#assumptions)

## Installation and Usage

1. To navigate to the `GIC_IAP_Assessment_ZhangChengChuan` folder, run `cd GIC_IAP_Assessment_ZhangChengChuan`.

2. On your virtual environment, run `pip install -r requirements.txt` to install the relevant libraries. Specifically, only `pickle`, `pytest`, and `json`.

3. To start the application, run `python3 main.py`.

4. To view the logs for system processes, they are recorded in `bank.log`.

5. To use the tests, run `pytest frontend_tests.py` or `pytest backend_tests.py`

## Design

1. **3 Layer application**: This application has a "pseudo" frontend (FE), backend (BE), and database (DB). This is to enable more efficient scaling of the application. As this code is meant to be run on a single machine, the frontend and backend are linked such that a request sent by the FE will trigger the BE to process the query, which I understand is not representative of real-life applications. To simplify the application, the DB is represented as just a simple JSON file.

2. **Queue and Queue Driver**: I implemented a Queue which stores the requests that come from the FE. The Queue Driver ideally should be running on a different machine, which constantly listens and observes the Queue. This queue enables asynchronous communication between FE and BE, allowing the FE to continue processing user input while the backend executes the commands. It also provides a buffer for handling traffic surges (when scaled to multiple users), ensuring that the backend can handle incoming requests at its own pace.

3. **Command Design Pattern**: I leverage the Command Design Pattern to encapsulate the specific operations the user wants to perform, such as deposits or withdrawals. By using the Command Pattern, I can easily extend the application with new operations in the future without affecting the existing codebase.

## Assumptions

I have heavily simplified many implementations of the application due to time and problem constraints, to the point where there are notable security errors and software engineering practices. Let me address them:

1. **Assumption of single-threaded machine**: Due to the sequential nature of my application, a multi-threaded machine will cause race conditions to occur. For example, when fetching a snapshot of the DB, should another change occur AFTER the initial snapshot of the DB, this will lead to disastrous consequences as the balance and transactions reflected are no longer accurate.

2. **No persistence of data**: The application assumes a fresh instance each time. Thus the previous user will not have their data persisted.

3. **Single user**: Due to (1) and (2), I assume there is only one user at any one time using this application.

4. **Use of same Queue and DB for testing**: This is definitely an issue to address, but due to limitations, I have used the `Queue.txt` and `DB.json` for both testing and production. However, with the assumptions made in (1), (2), and (3), I have decided to go ahead.