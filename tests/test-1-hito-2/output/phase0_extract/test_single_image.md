# Test

![Diagram](img/img_12.png)

> **Descripción del diagrama:**
> ### Diagram Type
This is a **Sequence Diagram**. Sequence diagrams are used to model the interactions between objects in a specific sequence of events. They show how objects interact with each other and the order in which these interactions occur.

### Main Elements and Their Attributes/Labels

1. **Participants (Lifelines):**
   - **Admin. Gestión Usuarios (Administrator User Management):** Represented by a stick figure icon, indicating a human actor or an external system.
   - **IGestiónUsuarios:** Represented by a circle with a line through it, indicating an interface or boundary object.
   - **ControlGestionUsuarios:** Represented by a circle with a spiral, indicating a control object.
   - **Usuario (User):** Represented by a circle, indicating an entity object.

2. **Messages:**
   - **DesactivarCuenta():** A synchronous message sent from "Admin. Gestión Usuarios" to "ControlGestionUsuarios."
   - **VerificarActividadCuenta():** A synchronous message sent from "ControlGestionUsuarios" to "Usuario."
   - **MensajeError():** An asynchronous message returned from "IGestiónUsuarios" to "Admin. Gestión Usuarios."
   - **MensajeOk():** An asynchronous message returned from "IGestiónUsuarios" to "Admin. Gestión Usuarios."

3. **Combined Fragments:**
   - **alt (Alternative):** Indicates an alternative flow based on a condition. It has two branches:
     - **Cuenta=!Activa:** If the account is not active, the flow proceeds to "MensajeError()" and then back to "Admin. Gestión Usuarios."
     - **Cuenta==Activa:** If the account is active, the flow proceeds to "MensajeOk()" and then back to "Admin. Gestión Usuarios."

4. **Activation Bars:**
   - Vertical bars on the lifelines indicate the period during which an object is performing an action or is active.

5. **Title:**
   - **CU-011 GESTIONAR USUARIO:** The title of the use case being depicted in the sequence diagram.

### Relationships and Multiplicities

- **Relationships:**
  - The "Admin. Gestión Usuarios" interacts with "ControlGestionUsuarios" to deactivate a user account.
  - "ControlGestionUsuarios" checks the activity status of the user account with "Usuario."
  - Based on the account status, "IGestiónUsuarios" sends either an error message or an OK message back to "Admin. Gestión Usuarios."

- **Multiplicities:**
  - The diagram does not explicitly show multiplicities as it is a sequence diagram focusing on the order of messages rather than the number of instances involved.

### Notation Used

- **Lifelines:** Dashed lines represent the lifelines of the participants.
- **Messages:** Solid arrows with filled arrowheads represent synchronous messages, while dashed arrows with open arrowheads represent asynchronous messages.
- **Activation Bars:** Rectangles on the lifelines indicate the duration of an object's activity.
- **Combined Fragments:** Enclosed boxes with labels like "alt" indicate conditional logic in the sequence.
- **Notes:** Small notes attached to the lifelines provide additional context or conditions for the flow.

### Detailed Description

The sequence diagram illustrates the process of managing a user account, specifically the deactivation of a user account. The process begins with the "Admin. Gestión Usuarios" initiating the "DesactivarCuenta()" message to the "ControlGestionUsuarios." The "ControlGestionUsuarios" then checks the account's activity status by sending a "VerificarActividadCuenta()" message to the "Usuario."

Based on the account's status, the "IGestiónUsuarios" returns a message to the "Admin. Gestión Usuarios":
- If the account is not active ("Cuenta=!Activa"), an error message ("MensajeError()") is returned.
- If the account is active ("Cuenta==Activa"), an OK message ("MensajeOk()") is returned.

This sequence ensures that the administrator is informed about the status of the account after attempting to deactivate it, providing clear feedback on whether the operation was successful or if there was an issue due to the account's current state. The use of the "alt" combined fragment effectively models the conditional logic based on the account's activity status.


Some text.