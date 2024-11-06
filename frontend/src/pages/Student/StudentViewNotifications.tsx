import axios from "axios";
import { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";

const StudentViewNotification = () => {
  const [notifications, setNotifications] = useState([]);
  const [errorMessage, setErrorMessage] = useState("");
  const navigate = useNavigate()
  const user_id = localStorage.getItem('user_id')

  useEffect(() => {
    const fetchNotifications = async () => {
      try {
        const response = await axios.post(
          `http://localhost:8000/view_notifications`,
          {
            user_id: user_id
          },
          {
            headers: { 'Content-Type': 'application/json' },
            withCredentials: false
          }
        );
        setNotifications(response.data.notifications);  // Set retrieved notifications in state
      } catch (error: any) {
        if (error.response) {
          console.error('Error fetching notifications:', error.response.data.message);
          setErrorMessage(error.response.data.detail || "Failed to fetch notifications");
        } else {
          console.error('An error occurred:', error.message);
          setErrorMessage("An unexpected error occurred.");
        }
      }
    };

    fetchNotifications();
  }, []);

  const handleSeen = async () => {
    try {
       await axios.post(
        `http://localhost:8000/delete_notifications`,
        {
          user_id: user_id
        },
        {
          headers: { 'Content-Type': 'application/json' },
          withCredentials: false
        }
      );
    } catch (error: any) {
      if (error.response) {
        console.error('Error deleting notifications:', error.response.data.message);
        setErrorMessage(error.response.data.detail || "Failed to delete notifications");
      } else {
        console.error('An error occurred:', error.message);
        setErrorMessage("An unexpected error occurred.");
      }
    }
  };

  return (
    <div>
      <h3>Notifications for {user_id} </h3>

      {errorMessage && <p style={{ color: "red" }}>{errorMessage}</p>}

      {notifications.length > 0 ? (
        <table style={{ borderCollapse: "collapse", width: "100%" }}>
        <thead>
          <tr>
            <th style={{ border: "1px solid black", padding: "8px" }}>Notification</th>
            <th style={{ border: "1px solid black", padding: "8px" }}>Timestamp</th>
          </tr>
        </thead>
        <tbody>
          {notifications.map((notification: any) => (
            <tr key={notification.course_id}>
              <td style={{ border: "1px solid black", padding: "8px" }}>{notification.notification_message}</td>
              <td style={{ border: "1px solid black", padding: "8px" }}>{notification.timestamp}</td>
            </tr>
          ))}
        </tbody>
      </table>
      ) : (
        <p>No Unread notifications</p>
      )}
        <div onClick={() => { handleSeen(); navigate(-1); }}>
  Go back
</div>

    </div>
  );
};

export default StudentViewNotification;
