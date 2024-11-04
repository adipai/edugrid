import axios from 'axios';
import React, { useEffect, useState } from 'react';

type QueryResult = {
    first_name: string;
    last_name: string;
    role: string;
    course_id: string;
};

const QueryFacultyAndTas: React.FC = () => {
    const [queryResult, setQueryResult] = useState<QueryResult[]>([]);

    const fetchData = async () => {
        try {
          const response = await axios.get(
            `http://localhost:8000/faculty_and_tas`
          );
          setQueryResult(response.data.faculty_and_tas);
        } catch (error) {
          console.error("Error fetching chapter details:", error);
        }
      };

    useEffect(() => {
        fetchData();
    }, []);

    return (
        <div>
            <table style={{ border: '1px solid black', borderCollapse: 'collapse' }}>
                <thead>
                    <tr>
                        <th style={{ border: '1px solid black', padding: '8px' }}>First Name</th>
                        <th style={{ border: '1px solid black', padding: '8px' }}>Last Name</th>
                        <th style={{ border: '1px solid black', padding: '8px' }}>Faculty</th>
                        <th style={{ border: '1px solid black', padding: '8px' }}>Course ID</th>
                    </tr>
                </thead>
                <tbody>
                    {queryResult.map((result, index) => (
                        <tr key={index}>
                            <td style={{ border: '1px solid black', padding: '8px' }}>{result.first_name}</td>
                            <td style={{ border: '1px solid black', padding: '8px' }}>{result.last_name}</td>
                            <td style={{ border: '1px solid black', padding: '8px' }}>{result.role}</td>
                            <td style={{ border: '1px solid black', padding: '8px' }}>{result.course_id}</td>
                        </tr>
                    ))}
                </tbody>
            </table>
        </div>
    );
};

export default QueryFacultyAndTas;