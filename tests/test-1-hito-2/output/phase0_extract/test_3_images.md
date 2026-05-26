# Test

![Img1](img/img_12.png)

> **Descripción del diagrama:**
> ### Diagram Type
This is a **Sequence Diagram**. Sequence diagrams are used to model the interactions between objects in a specific sequence of events. They show how objects interact with each other and the order in which these interactions occur.

### Main Elements and Their Attributes/Labels

1. **Admin. Gestión Usuarios (Administrator User Management)**
   - Represented by a stick figure icon.
   - Acts as the initiator of the process.
   - Has a vertical lifeline indicating its active participation in the sequence.

2. **IGestiónUsuarios (User Management Interface)**
   - Represented by a circular icon.
   - Receives messages from the Administrator User Management.
   - Has a vertical lifeline.

3. **ControlGestionUsuarios (User Management Control)**
   - Represented by a circular icon.
   - Receives messages from the User Management Interface.
   - Performs actions and sends responses back.
   - Has a vertical lifeline.

4. **Usuario (User)**
   - Represented by a circular icon.
   - Receives messages from the User Management Control.
   - Has a vertical lifeline.

### Relationships and Multiplicities

- **Admin. Gestión Usuarios** initiates the process by sending a message to **IGestiónUsuarios**.
- **IGestiónUsuarios** then sends a message to **ControlGestionUsuarios**.
- **ControlGestionUsuarios** performs an action and sends a response back to **IGestiónUsuarios**.
- **IGestiónUsuarios** then sends a response back to **Admin. Gestión Usuarios**.
- There is a conditional flow based on the state of the user account:
  - If the account is not active (`Cuenta=!Activa`), an error message is sent back to the Administrator User Management.
  - If the account is active (`Cuenta==Activa`), an OK message is sent back to the Administrator User Management.

### Notation Used

- **Lifelines**: Vertical dashed lines represent the existence of an object over time.
- **Activation Bars**: Blue rectangles on the lifelines indicate the period during which an object is performing an action.
- **Messages**: Arrows represent the communication between objects.
  - Solid arrows with filled arrowheads indicate synchronous messages.
  - Dashed arrows with open arrowheads indicate return messages or asynchronous messages.
- **Alt Combined Fragment**: A rectangular box labeled "alt" represents an alternative path in the sequence, depending on a condition.
- **Note**: Small rectangular boxes with text inside provide additional information or conditions.

### Visible Text or Titles

- **Title**: "CU-011 GESTIONAR USUARIO" (Manage User)
- **Process Name**: "sd Desactivar Cuenta" (Deactivate Account)
- **Messages**:
  - "1. DesactivarCuenta()" (Deactivate Account)
  - "2. VerificarActividadCuenta()" (Verify Account Activity)
  - "2.1 MensajeError()" (Error Message)
  - "2.2 MensajeError()" (Error Message)
  - "2.3 MensajeOk()" (OK Message)
  - "2.4 MensajeOk()" (OK Message)

### Detailed Description

The sequence diagram illustrates the process of deactivating a user account within a system. The Administrator User Management initiates the process by sending a "DesactivarCuenta()" message to the User Management Interface. The User Management Interface then forwards this request to the User Management Control, which checks the account activity.

Based on the account's status:
- If the account is not active (`Cuenta=!Activa`), the User Management Control sends an error message back to the User Management Interface, which then relays it to the Administrator User Management.
- If the account is active (`Cuenta==Activa`), the User Management Control sends an OK message back to the User Management Interface, which then relays it to the Administrator User Management.

The diagram effectively captures the step-by-step interaction between the different components involved in managing user accounts, highlighting the conditional logic based on the account's status. This helps in understanding the flow of control and the responsibilities of each component in the system.


![Img2](img/img_13.png)

> **Descripción del diagrama:**
> The diagram provided is a **Sequence Diagram**, which is a type of interaction diagram used in UML (Unified Modeling Language) to describe how objects interact with each other over time. It shows the sequence of messages exchanged between objects to perform a specific operation or achieve a particular goal.

---

### 1. **Main Elements and Their Attributes/Labels**

The diagram includes the following main elements:

- **Participants (Lifelines):**
  - **Admin. Gestión Usuarios** (Administrator User Management): Represented by a stick figure, indicating a human actor or user role.
  - **IGestiónUsuarios** (User Management Interface): Represented by a circle with a horizontal line, indicating an interface or boundary object.
  - **ControlGestionUsuarios** (User Management Control): Represented by a circle with a curved arrow, indicating a control object that manages the logic.
  - **Usuario** (User): Represented by a circle, indicating an entity or data object.

Each participant has a vertical dashed line extending downward, representing their lifeline, which shows the duration of their existence during the interaction.

- **Messages:**
  - **ActivarCuenta()**: A synchronous message sent from "Admin. Gestión Usuarios" to "ControlGestionUsuarios," indicating the activation of a user account.
  - **VerificarActividadCuenta()**: A synchronous message sent from "ControlGestionUsuarios" to "Usuario," indicating a check for the account's activity status.
  - **MensajeError()**: An asynchronous message returned from "Usuario" to "IGestiónUsuarios," indicating an error message.
  - **MensajeOk()**: An asynchronous message returned from "IGestiónUsuarios" to "Admin. Gestión Usuarios," indicating a successful operation.

- **Conditional Blocks (alt):**
  - The diagram includes two conditional blocks labeled "alt," which represent alternative paths based on conditions:
    - **Cuenta==Activa**: If the account is active, the flow proceeds to "MensajeError()" being sent back to "IGestiónUsuarios."
    - **Cuenta!=Activa**: If the account is not active, the flow proceeds to "MensajeOk()" being sent back to "Admin. Gestión Usuarios."

- **Title:**
  - The title of the diagram is "CU-011 GESTIONAR USUARIO," which translates to "Use Case 011 Manage User." This indicates that the diagram describes the sequence of interactions for managing a user account.

- **Reference:**
  - The label "sd Activar Cuenta" at the top left corner suggests that this diagram is a reference for the "Activate Account" use case.

---

### 2. **Relationships and Multiplicities**

- **Relationships:**
  - The relationships between the participants are represented by messages exchanged in a sequential manner. Each message corresponds to a method call or response.
  - The "alt" block introduces conditional relationships, where the flow of messages depends on the state of the account (active or inactive).

- **Multiplicities:**
  - The diagram does not explicitly show multiplicities (e.g., 1..* or 0..1) because it focuses on the sequence of interactions rather than the number of instances involved. However, the lifelines suggest that each participant exists for the duration of the interaction.

---

### 3. **Notation Used**

- **Lifelines:** Vertical dashed lines represent the existence of each participant over time.
- **Activation Bars:** Blue rectangles on the lifelines indicate the period during which a participant is actively performing an operation.
- **Messages:** Solid arrows with filled arrowheads represent synchronous messages (method calls), while dashed arrows with open arrowheads represent asynchronous messages (returns or responses).
- **Conditional Blocks (alt):** Rectangles labeled "alt" with conditions inside them represent alternative paths in the sequence. Each path is separated by a dashed horizontal line.
- **Self-Message:** The "VerificarActividadCuenta()" message is a self-message, indicated by an arrow looping back to the same participant ("ControlGestionUsuarios"), showing that the control object performs an internal check.

---

### 4. **Visible Text or Titles**

- **Diagram Title:** "CU-011 GESTIONAR USUARIO" (Use Case 011 Manage User).
- **Participant Labels:**
  - Admin. Gestión Usuarios
  - IGestiónUsuarios
  - ControlGestionUsuarios
  - Usuario
- **Message Labels:**
  - ActivarCuenta()
  - VerificarActividadCuenta()
  - MensajeError()
  - MensajeOk()
- **Condition Labels:**
  - Cuenta==Activa
  - Cuenta!=Activa
- **Reference Label:** "sd Activar Cuenta"

---

### 5. **Summary Description**

This Sequence Diagram illustrates the process of managing a user account, specifically focusing on the activation of a user account. The diagram shows the interaction between four key components: the administrator, the user management interface, the control logic, and the user entity. The sequence begins with the administrator initiating the account activation, followed by a check for the account's activity status. Based on the account's status (active or inactive), the system responds with either an error message or a success message. The "alt" block highlights the conditional nature of the response, ensuring that the appropriate message is sent depending on the account's state. The diagram is part of a larger use case, "Activate Account," as indicated by the reference label.


![Img3](img/img_16.png)

> **Descripción del diagrama:**
> ### 1. **Type of Diagram**
This is a **Sequence Diagram**, which is a type of interaction diagram used in UML (Unified Modeling Language). It illustrates the order of interactions between objects or participants in a system over time, showing how messages are passed between them to achieve a specific goal.

---

### 2. **Main Elements and Their Attributes/Labels**

The diagram includes the following key elements:

#### **Participants (Lifelines):**
1. **Admin. Gestión Usuarios**:
   - Represented by a stick figure icon.
   - Acts as the initiator of the process.
   - Labeled as "sd ref" at the top, indicating a reference to a system description.

2. **IGestiónUsuarios**:
   - Represented by a circular icon with a horizontal line.
   - Likely represents an interface for managing users.

3. **ControlGestionUsuarios**:
   - Represented by a circular icon with a spiral arrow.
   - Likely represents a control component responsible for managing user data.

4. **Usuario**:
   - Represented by a circular icon.
   - Represents the user entity or object being managed.

#### **Messages (Arrows):**
- Messages are represented by arrows between lifelines, indicating the flow of communication.
- Each message is labeled with a number and a description of the action being performed.

#### **Fragments:**
- **alt (Alternative)**:
  - A rectangular box with a dashed border.
  - Contains two alternative paths based on a condition:
    - `{datos validos}` (valid data)
    - `{datos incorrectos}` (incorrect data)

- **loop (Loop)**:
  - A rectangular box with a dashed border.
  - Indicates a repeated sequence of actions, typically used when data is incorrect and needs to be re-entered.

#### **Titles and Labels:**
- **Title**: "CU-011 GESTIONAR USUARIO"
  - This is the main title of the use case, indicating that the diagram describes the process of managing a user.
- **Subtitles**:
  - "sd Modificar Usuario" (System Description: Modify User)
  - "sd ref" (System Description Reference)

---

### 3. **Relationships and Multiplicities**

- **Relationships**:
  - The relationships between participants are shown through the sequence of messages exchanged.
  - The `Admin. Gestión Usuarios` initiates the process by sending a message to `IGestiónUsuarios`.
  - `IGestiónUsuarios` then interacts with `ControlGestionUsuarios` to verify and modify data.
  - If the data is valid, a confirmation message is sent back to `Admin. Gestión Usuarios`.
  - If the data is incorrect, the process loops back to request new data.

- **Multiplicities**:
  - The diagram does not explicitly show multiplicities (e.g., 1..*), but the loop fragment implies that the process can repeat multiple times if data is incorrect.

---

### 4. **Notation Used**

- **Lifelines**:
  - Vertical dashed lines represent the lifelines of each participant, showing their existence over time.
  - Activation bars (thick vertical rectangles) indicate when a participant is actively performing an operation.

- **Messages**:
  - Solid arrows with filled arrowheads represent synchronous messages (e.g., method calls).
  - Dashed arrows with open arrowheads represent return messages or asynchronous communication.

- **Fragments**:
  - **alt**: Used to represent alternative paths based on a condition.
  - **loop**: Used to represent a repeated sequence of actions.

- **Text Labels**:
  - Each message is labeled with a number and a description (e.g., "1. ModificarCuenta()").
  - Conditions for alternative paths are written inside curly braces (e.g., `{datos validos}`).

---

### 5. **Visible Text and Titles**

- **Main Title**: "CU-011 GESTIONAR USUARIO"
  - This is the primary focus of the diagram, indicating the use case being described.

- **Subtitles**:
  - "sd Modificar Usuario" (System Description: Modify User)
  - "sd ref" (System Description Reference)

- **Message Labels**:
  - "1. ModificarCuenta()"
  - "1.1 SolicitarDatos()"
  - "1.1.2 SolicitarDatos()"
  - "2. IngresarDatos()"
  - "2.1 IngresarDatos()"
  - "3. VerificarDatos()"
  - "3.2 MensajeOk()"
  - "3.1 ModificarDatos()"
  - "4.1 SolicitarDatos()"
  - "4. SolicitarDatos()"

- **Conditions**:
  - "{datos validos}" (valid data)
  - "{datos incorrectos}" (incorrect data)

---

### 6. **Description of the Process**

The diagram illustrates the process of modifying a user account in a system. Here's a step-by-step breakdown:

1. **Initiation**:
   - The `Admin. Gestión Usuarios` initiates the process by sending a message to `IGestiónUsuarios` to modify the user account (`1. ModificarCuenta()`).

2. **Data Request**:
   - `IGestiónUsuarios` requests data from the `Usuario` (`1.1 SolicitarDatos()`).

3. **Data Entry**:
   - The `Admin. Gestión Usuarios` enters the data (`2. IngresarDatos()`), which is then passed to `IGestiónUsuarios` (`2.1 IngresarDatos()`).

4. **Data Verification**:
   - `IGestiónUsuarios` sends the data to `ControlGestionUsuarios` for verification (`3. VerificarDatos()`).

5. **Validation Check**:
   - If the data is valid (`{datos validos}`), a confirmation message (`3.2 MensajeOk()`) is sent back to `Admin. Gestión Usuarios`.

6. **Data Modification**:
   - If the data is valid, `ControlGestionUsuarios` modifies the data (`3.1 ModificarDatos()`) and sends it back to the `Usuario`.

7. **Incorrect Data Handling**:
   - If the data is incorrect (`{datos incorrectos}`), the process loops back to request new data (`4.1 SolicitarDatos()` and `4. SolicitarDatos()`).

---

### 7. **Summary**

This Sequence Diagram effectively models the interaction between different components of a system during the process of managing a user account. It highlights the flow of messages, the conditions under which different paths are taken, and the roles of each participant in the system. The use of fragments (`alt` and `loop`) allows for a clear representation of alternative and repetitive processes, making it easier to understand the system's behavior under different scenarios.

