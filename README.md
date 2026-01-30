## 🏗️ Architecture Diagram

<img width="1605" height="1094" alt="image" src="https://github.com/user-attachments/assets/bd7d9b86-f0d7-4f08-8dd9-000438aa20c5" />



--

## 📌 Overview

Modern applications require fast, intelligent customer support without manual intervention.  
This project solves that by:

- Accepting customer feedback via a web UI
- Using AI to analyze sentiment and urgency
- Automatically acknowledging customers
- Escalating high-priority issues to support teams
- Persisting tickets for tracking and auditing

All components are **fully serverless**, scalable, and loosely coupled.

---

## 🧠 Key Features

- ✅ AI-based sentiment & urgency detection (Amazon Bedrock)
- ✅ Automated customer acknowledgment email
- ✅ Conditional escalation for high-priority tickets
- ✅ Email & SMS alerts to support team
- ✅ Persistent ticket storage (DynamoDB)
- ✅ Orchestrated workflow using Step Functions
- ✅ Secure REST API backend
- ✅ Modular, production-style frontend
- ✅ Zero server management



## 🏗️ Architecture



Frontend (S3 / Local UI)
|
v
API Gateway (REST API)
|
v
AWS Step Functions
|
+--> Validate Input (Lambda)
|
+--> Analyze Feedback (AI – Bedrock)
|
+--> Generate Auto Response (AI – Bedrock)
|
+--> Store Ticket (DynamoDB)
|
+--> [Choice State]
|
+--> High Urgency → Notify Support (SNS Email + SMS)
|
+--> Normal → End
|
+--> Send Customer Acknowledgment (SES)

````

---

## 🧰 Tech Stack

### Frontend
- HTML5
- CSS3 (professional grey-based UI)
- JavaScript (Fetch API)

### Backend & Cloud
- **AWS API Gateway** – REST API
- **AWS Lambda** – Business logic
- **AWS Step Functions** – Workflow orchestration
- **Amazon DynamoDB** – Ticket storage
- **Amazon SNS** – Support email & SMS alerts
- **Amazon SES** – Customer acknowledgment emails
- **Amazon Bedrock** – AI sentiment analysis & response generation
- **AWS IAM** – Secure access control

---

## 🧪 Workflow Explanation

1. **User submits feedback** through UI
2. **API Gateway** triggers Step Functions
3. **ValidateInput Lambda**
   - Ensures email & feedback exist
4. **AnalyzeFeedback Lambda**
   - Uses AI to determine sentiment & urgency
5. **GenerateAutoResponse Lambda**
   - Generates polite customer acknowledgment using AI
6. **StoreTicket Lambda**
   - Stores ticket data in DynamoDB
7. **Choice State**
   - If urgency = High → notify support
8. **NotifySupport Lambda**
   - Sends email & SMS to support team
9. **SendCustomerResponse Lambda**
   - Sends auto-response email to customer

---

## 🧠 AI Usage Details

Amazon Bedrock is used for:
- **Sentiment classification** (Positive / Neutral / Negative)
- **Urgency detection** (Low / Medium / High)
- **Customer response generation**

AI outputs are safely parsed and validated before use.

---

## 📬 Notification Strategy

| Recipient | Service | Reason |
|---------|--------|-------|
| Customer | SES | Dynamic, per-user email |
| Support Team | SNS | Fixed subscribers |
| Support SMS | SNS | Immediate alert |

This separation reflects **real production best practices**.

---

## 🗄️ DynamoDB Data Model

Example item:

```json
{
  "ticket_id": "TICKET-12345",
  "email": "user@example.com",
  "feedback": "Payment deducted twice",
  "sentiment": "Negative",
  "urgency": "High",
  "timestamp": "2026-01-29T18:45:00Z"
}
````

---

## 🔐 Security Considerations

* IAM roles with **least privilege**
* No credentials committed to GitHub
* `.gitignore` used for secrets
* API Gateway CORS configured safely
* SES sandbox / production handled correctly

---

## 💰 Cost Considerations

This project is **very low cost**:

* Lambda → Pay per invocation
* Step Functions → Per state transition
* DynamoDB → On-demand
* SNS / SES → Minimal usage
* Bedrock → Used only during analysis

Ideal for learning, demos, and interviews.

---

## 🧪 Testing

### Manual Tests

* API tested using Postman
* Step Function executions monitored
* DynamoDB entries verified
* Email & SMS delivery confirmed

### Error Handling

* Missing inputs rejected early
* AI parsing safeguarded
* Notification failures isolated

---

## 🚀 How to Run Locally (Frontend)

1. Open `index.html`
2. Enter:

   * Email
   * Feedback
3. Submit form
4. Observe:

   * Success message
   * Email acknowledgment
   * Support alert (if high urgency)

---

## 📂 Repository Structure

```
.
├── frontend/
│   ├── index.html
│   ├── style.css
│   └── script.js
│
├── lambdas/
│   ├── validate-input/
│   ├── analyze-feedback/
│   ├── generate-auto-response/
│   ├── store-ticket/
│   ├── notify-support/
│   └── send-customer-response/
│
├── step-functions/
│   └── smart-support-workflow.json
│
└── README.md
```


## 📈 Possible Enhancements

* Admin dashboard for tickets
* CloudWatch alarms
* Multi-language support
* Authentication (Cognito)
* Ticket status updates
* Analytics & reporting

---

## 👨‍💻 Author

**Lalit Pandey**
AWS | Cloud | Serverless | AI Enthusiast

GitHub: [https://github.com/LalitPandey12911](https://github.com/LalitPandey12911)



---

