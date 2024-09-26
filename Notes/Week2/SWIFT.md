# SWIFT Notes

The **SWIFT (Society for Worldwide Interbank Financial Telecommunication)** financial messaging system is a secure global platform used by financial institutions to exchange standardized financial messages. SWIFT connects thousands of banks, financial institutions, and corporations in over 200 countries, facilitating the transmission of payment orders, securities transactions, trade finance instructions, and other financial information in a secure and reliable manner.

Here’s how it works:

## Key Components

1. **Messaging Network**: SWIFT provides a platform for financial institutions to send and receive standardized messages (such as payment instructions, confirmations, account statements, etc.) securely. It does not hold or transfer funds but ensures that financial information between banks is communicated securely.

2. **Message Standards**: SWIFT uses a set of standard formats (such as **MT messages** and the newer **ISO 20022** format) to ensure that financial institutions can communicate in a universally understood language.

3. **SWIFT Code/BIC**: Each institution connected to SWIFT has a unique identifier known as a **SWIFT code** or **Bank Identifier Code (BIC)**. This ensures that messages are routed to the correct institution.

## How SWIFT Works

- A bank that wants to send a payment instruction to another bank composes a SWIFT message in a standardized format and sends it over the SWIFT network.
- The recipient bank receives the message and processes the payment based on the instructions contained in the message.
- The entire process is done securely, with encryption and strict compliance standards, reducing the risk of fraud or miscommunication.

## Why SWIFT Is Important

1. **Global Reach**: SWIFT connects over 11,000 financial institutions worldwide, making it the most widely used network for cross-border payments and international trade.
2. **Security**: The platform ensures secure transmission of sensitive financial information, using encryption and other security protocols to prevent unauthorized access.
3. **Standardization**: SWIFT’s message standards ensure that banks and financial institutions can exchange information in a consistent format, reducing errors and processing times.
4. **Reliability**: SWIFT is known for its robust infrastructure, offering high availability and fast, secure communication channels between financial institutions.

In essence, SWIFT plays a vital role in global finance by providing the backbone for the secure transfer of financial data between institutions.

A **SWIFT message** follows a specific format, depending on the type of message being transmitted. The most commonly used format for financial transactions is the **MT (Message Type)** format. Each SWIFT message consists of various parts, called blocks, which are used to structure the information. Here’s a breakdown of the general structure of a SWIFT message:

## General Structure of an MT (Message Type) SWIFT Message

1. **Basic Block Structure**:
   A SWIFT MT message is structured in blocks, which are enclosed in curly braces `{}`. Each block has a specific function and contains various fields, with specific formats depending on the message type.

   The basic block structure of an MT message consists of:
   - **Block 1**: Basic Header
   - **Block 2**: Application Header
   - **Block 3**: User Header (optional)
   - **Block 4**: Text Block (the actual content of the message)
   - **Block 5**: Trailer (optional)

---

### Detailed Block Breakdown

#### **Block 1: Basic Header**

- Contains essential information about the sender and the message itself.
- Example format: `{1:F01BANKBEBBAXXX1234567890}`
  - **F**: Stands for Financial message.
  - **01**: Denotes message type (always 01 for SWIFT).
  - **BANKBEBBAXXX**: SWIFT code of the sender (BIC).
  - **1234567890**: Session and sequence number.

#### **Block 2: Application Header**

- Defines the message type and its intended receiver.
- Example format: `{2:I100BANKDEFFXXXXU3003}`
  - **I**: Denotes the input (for outgoing message).
  - **100**: The message type (e.g., MT100 for payment messages).
  - **BANKDEFFXXXX**: SWIFT code of the receiver.
  - **U**: Urgency (Normal: N, Priority: P, Urgent: U).
  - **3003**: Message sequence number.

#### **Block 3: User Header (Optional)**

- This block contains additional information such as the message priority or special instructions.
- Example: `{3:{113:1234567890}{119:STP}}`
  - **113**: Message reference.
  - **119**: STP (Straight-Through Processing) code for automated processing.

#### **Block 4: Text Block**

- This block contains the actual transaction data, like the amount, currency, account numbers, and other details.
- Format: `{4:<message content>}`
- The content inside block 4 will vary depending on the message type. For example, an MT103 (customer payment) might include:

     ```
     {4:
     :20:1234567890
     :32A:210924USD10000,
     :50K:/1234567890
     John Doe
     123 Main St
     New York
     :59:/9876543210
     Jane Smith
     456 Maple Ave
     Los Angeles
     }
     ```

  - **:20:** Transaction reference number.
  - **:32A:** Value date, currency, and amount.
  - **:50K:** Ordering customer details (account, name, address).
  - **:59:** Beneficiary customer details (account, name, address).

#### **Block 5: Trailer Block (Optional)**

- Contains security and message validation information (e.g., MAC, checksum).
- Example: `{5:{CHK:123456789ABC}}`
  - **CHK**: Checksum value to verify message integrity.

---

### Example of a Complete SWIFT MT103 Message

```
{1:F01BANKBEBBAXXX1234567890}
{2:I103BANKDEFFXXXXN}
{3:{113:1234567890}{119:STP}}
{4:
:20:1234567890
:23B:CRED
:32A:210924USD10000,
:50K:/1234567890
John Doe
123 Main St
New York
:59:/9876543210
Jane Smith
456 Maple Ave
Los Angeles
:71A:SHA
}
{5:{CHK:123456789ABC}}
```

- **Block 1**: Message from `BANKBEBBAXXX` to `BANKDEFFXXXX`, session number `1234567890`.
- **Block 2**: Message type MT103 (customer payment).
- **Block 3**: Message reference and STP indicator.
- **Block 4**: Contains the actual transaction details (sender, receiver, amount, etc.).
- **Block 5**: Message checksum for validation.

---

### Common MT Message Types

- **MT103**: Customer payment (single transaction).
- **MT202**: Bank-to-bank payment transfer.
- **MT910**: Confirmation of credit.
- **MT940**: Customer statement message.
- **MT950**: Statement message.

---

### **Category 1: Customer Payments and Cheques**

1. **MT103** – Single customer credit transfer (used for international wire transfers).
2. **MT101** – Request for transfer (used to instruct a bank to transfer funds on behalf of the customer).
3. **MT104** – Direct debit and request for debit transfer.
4. **MT110** – Advice of cheque(s).

---

### **Category 2: Financial Institution Transfers**

1. **MT200** – Financial institution transfer for its own account.
2. **MT202** – General financial institution transfer (bank-to-bank transfers, often for settlement).
3. **MT202 COV** – Financial institution transfer with cover (associated with underlying payment transactions like MT103).
4. **MT203** – Multiple financial institution transfers.
5. **MT205** – Financial institution transfer executed via third-party financial institutions.

---

### **Category 3: Treasury Markets and Forex**

1. **MT300** – Foreign exchange confirmation.
2. **MT320** – Fixed loan/deposit confirmation.
3. **MT330** – Call/notice loan/deposit confirmation.
4. **MT340** – Forward rate agreement (FRA) confirmation.
5. **MT360** – Interest rate derivative confirmation.

---

### **Category 4: Collection and Cash Letters**

1. **MT400** – Advice of payment (used in documentary collections).
2. **MT410** – Acknowledgment of receipt of a collection.
3. **MT412** – Advice of acceptance or non-acceptance (regarding payment instruments).
4. **MT416** – Advice of fate of a collection.
5. **MT422** – Advice of final payment.
6. **MT430** – Advice of dishonor (non-payment or non-acceptance).

---

### **Category 5: Securities Market**

1. **MT500** – Instruction to register securities.
2. **MT515** – Client confirmation of purchase/sale.
3. **MT535** – Statement of holdings.
4. **MT536** – Statement of transactions.
5. **MT540** – Receive free (instructions to receive securities without payment).
6. **MT541** – Receive against payment.
7. **MT542** – Deliver free.
8. **MT543** – Deliver against payment.

---

### **Category 6: Commodities and Syndicated Loans**

1. **MT600** – Commodity trade confirmation.
2. **MT601** – Commodity trade confirmation for non-deliverable forwards (NDF).
3. **MT604** – Commodity transfer allocation.
4. **MT605** – Commodity credit adjustment/debit adjustment.
5. **MT606** – Commodity interest payment.
6. **MT608** – Commodity settlement message.
7. **MT610** – Confirmation of loan/deposit.
8. **MT620** – Notice to drawdown.

---

### **Category 7: Documentary Credits and Guarantees**

1. **MT700** – Issue of a documentary credit (used in trade finance).
2. **MT701** – Amendment to a documentary credit.
3. **MT707** – Amendment to a previously issued MT700.
4. **MT710** – Advice of a third-party documentary credit.
5. **MT720** – Transfer of a documentary credit.
6. **MT730** – Acknowledgment of a documentary credit.
7. **MT740** – Authorization to reimburse.
8. **MT742** – Reimbursement claim.

---

### **Category 8: Travellers Cheques and Payments**

1. **MT800** – Traveller’s cheque issuance.
2. **MT802** – Traveller’s cheque settlement.
3. **MT810** – Request for traveller’s cheque issuance.
4. **MT820** – Traveller’s cheque encashment.
5. **MT830** – Traveller’s cheque refund.
6. **MT890** – Advice of traveller’s cheque stop payment.

---

### **Category 9: Cash Management and Customer Status**

1. **MT900** – Confirmation of debit (used to notify an account has been debited).
2. **MT910** – Confirmation of credit (used to notify an account has been credited).
3. **MT940** – Customer statement message (end-of-day statement).
4. **MT942** – Interim transaction report (real-time or intraday statements).
5. **MT950** – Statement message (account statement for a financial institution).
6. **MT999** – Free format message (for non-standard messages).

### Overview

The **SWIFT MT codes** cover a wide range of financial operations, and they are organized by category to facilitate standardized communication between banks. Each category corresponds to specific types of financial transactions or messages, with:

- **MT1xx**: Customer payments.
- **MT2xx**: Financial institution transfers.
- **MT3xx**: Forex and treasury markets.
- **MT4xx**: Collections and cash letters.
- **MT5xx**: Securities markets.
- **MT6xx**: Commodities and syndicated loans.
- **MT7xx**: Documentary credits and guarantees.
- **MT8xx**: Traveller’s cheques and related transactions.
- **MT9xx**: Cash management messages.

These codes standardize financial messaging globally, helping ensure secure, efficient, and transparent transactions across international banking systems.

### Code Documentation

[This link will take you to the SWIFT Knowledge Center, that has all the up to date documentation for the different MT code families.](https://www2.swift.com/knowledgecentre/products/Standards%20MT/publications#November%202024)
