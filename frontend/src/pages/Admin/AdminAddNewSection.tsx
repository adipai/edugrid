import React, { useEffect, useState } from "react";
import { Link, useLocation, useNavigate } from "react-router-dom";
import axios from 'axios';

const AdminAddNewSection: React.FC = () => {
  const [sectionNumber, setSectionNumber] = useState("");
  const [sectionTitle, setSectionTitle] = useState("");
  const [chapDetails, setChapDetails] = useState<any>({});
  const [tbDetails, setTbDetails] = useState<any>({});
  const location = useLocation();
  const queryParams = new URLSearchParams(location.search);
  const tb_id = queryParams.get("tb_id");
  const chap_id = queryParams.get("chap_id");
  const createdBy = localStorage.getItem('user_id')
  const navigate = useNavigate();


  useEffect(() => {
    // Fetch chapter data here
    fetch(`http://localhost:8000/api/v1/chapter?tb_id=${tb_id}&chap_id=${chap_id}`)
      .then((response) => response.json())
      .then((data) => {
        // Handle the fetched chapter data here
        setChapDetails(data.chapter)
      })
      .catch((error) => {
        console.error("Error fetching textbook data:", error);
      });
      fetch(`http://localhost:8000/api/v1/textbook?tb_id=${tb_id}`)
      .then((response) => response.json())
      .then((data) => {
        // Handle the fetched textbook data here
        setTbDetails(data.textbook);
      })
      .catch((error) => {
        console.error("Error fetching textbook data:", error);
      });
  }, [tb_id, chap_id]);

  const handleSubmit = async(e: React.FormEvent) => {
    e.preventDefault();
    // Handle form submission logic here
    console.log("Section Number:", sectionNumber);
    console.log("Section Title:", sectionTitle);
    try {
      const response = await axios.post('http://localhost:8000/create_section', {
          tb_id: tb_id,
          chap_id: chap_id,
          sec_id: sectionNumber,
          sec_name: sectionTitle,
          created_by: createdBy
      });
      console.log('Section created:', response.data);
      navigate('/admin/create-new-content-block?tb_id=' + tb_id + "&chap_id=" + chap_id + "&csec_id=" + sectionNumber);
  } catch (error) {
      console.error('Error creating section:', error);
  }
  };

  return (
    <div>
      <h1>Add New Section</h1>
      <form onSubmit={handleSubmit}>
      <h3>Textbook Name: {tbDetails?.title}</h3>
      <h3>Chapter Name: {chapDetails?.title}</h3>
        <div>
          <label htmlFor="sectionNumber">Section Number:</label>
          <input
            type="text"
            id="sectionNumber"
            value={sectionNumber}
            onChange={(e) => setSectionNumber(e.target.value)}
          />
        </div>
        <div>
          <label htmlFor="sectionTitle">Section Title:</label>
          <input
            type="text"
            id="sectionTitle"
            value={sectionTitle}
            onChange={(e) => setSectionTitle(e.target.value)}
          />
        </div>
        <button type="submit" onClick={(e) => handleSubmit(e)}>
          Add new section
        </button>
      </form>
      {/* <div>
        <Link to="/add-content-block">Add new content block</Link>
      </div> */}
      <div>
        {/* <Link to="/admin/landing">Go back</Link> */}
        <div onClick={() => navigate(-1)}>Go Back</div>
      </div>
      <div>
        <Link to="/admin/landing">Landing Page</Link>
      </div>
    </div>
  );
};

export default AdminAddNewSection;
