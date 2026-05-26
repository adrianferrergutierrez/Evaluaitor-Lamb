# Test
![Img1](img/img_3.png)

![Img2](img/img_6.png)

![Img3](img/img_9.png)

![Img4](img/img_12.png)

> **Descripción del diagrama:**
> The diagram provided is a **Sequence Diagram**, which is a type of interaction diagram used in UML (Unified Modeling Language) to describe how objects interact with each other over time. It shows the sequence of messages exchanged between objects to perform a specific operation or achieve a particular goal.

### Detailed Description:

#### 1. Main Elements and Their Attributes/Labels:

- **Participants (Lifelines):**
  - **Admin. Gestión Usuarios (Administrator User Management):** Represented by a stick figure icon, indicating a human actor or an external system that initiates the process.
  - **IGestiónUsuarios (User Management Interface):** Represented by a blue circle with a horizontal line, indicating an interface or boundary object that interacts with the user management system.
  - **ControlGestionUsuarios (User Management Control):** Represented by a blue circle with a curved arrow, indicating a control object that manages the flow of the process.
  - **Usuario (User):** Represented by a blue circle, indicating the user entity or object being managed.

- **Messages:**
  - **DesactivarCuenta():** A message sent from the Administrator User Management to the User Management Interface to deactivate a user account.
  - **VerificarActividadCuenta():** A message sent from the User Management Interface to the User Management Control to verify the account activity.
  - **MensajeError():** A return message sent from the User Management Control to the User Management Interface indicating an error.
  - **MensajeOk():** A return message sent from the User Management Control to the User Management Interface indicating success.

- **Combined Fragments:**
  - **alt (Alternative):** A combined fragment that represents alternative paths based on a condition. In this case, it checks whether the account is active or not.
    - **Cuenta=!Activa:** If the account is not active, the process sends a `MensajeError()` message.
    - **Cuenta==Activa:** If the account is active, the process sends a `MensajeOk()` message.

- **Title:**
  - **CU-011 GESTIONAR USUARIO:** The title of the use case, indicating that this sequence diagram is related to managing a user.

- **Frame:**
  - **sd Desactivar Cuenta:** A frame labeled "sd" (sequence diagram) that encapsulates the entire sequence of interactions for deactivating a user account.

#### 2. Relationships and Multiplicities:

- **Relationships:**
  - The relationships are represented by the messages exchanged between the participants. Each message indicates a call or return, showing the flow of control and data.
  - The `alt` fragment shows a conditional relationship where the flow depends on the state of the account (active or not).

- **Multiplicities:**
  - There are no explicit multiplicities shown in this diagram, as it focuses on the sequence of interactions rather than the number of instances of objects.

#### 3. Notation Used:

- **Lifelines:** Vertical dashed lines represent the lifelines of each participant, showing their existence over time.
- **Activation Bars:** Blue rectangles on the lifelines indicate the period during which an object is performing an action or is active.
- **Messages:** Solid arrows represent synchronous messages (calls), while dashed arrows represent return messages.
- **Combined Fragments:** Enclosed boxes with labels like `alt` indicate different scenarios or conditions that can occur during the interaction.
- **Condition Labels:** Text inside the `alt` fragment specifies the condition under which a particular path is taken.

#### 4. Visible Text or Titles:

- **Main Title:** "CU-011 GESTIONAR USUARIO" — This is the title of the use case being depicted.
- **Frame Label:** "sd Desactivar Cuenta" — This labels the sequence diagram as related to deactivating a user account.
- **Message Labels:** "DesactivarCuenta()", "VerificarActividadCuenta()", "MensajeError()", "MensajeOk()" — These labels describe the actions and responses in the sequence.
- **Condition Labels:** "Cuenta=!Activa" and "Cuenta==Activa" — These specify the conditions for the alternative paths.

### Summary:

This Sequence Diagram illustrates the process of deactivating a user account within a system. It shows the interaction between the administrator, the user management interface, the control logic, and the user entity. The diagram uses a combination of messages, activation bars, and a conditional fragment (`alt`) to depict the flow of control and the possible outcomes based on the account's status. The overall purpose is to manage user accounts, specifically focusing on the deactivation process and handling errors or successful operations accordingly.


![Img5](img/img_15.png)

