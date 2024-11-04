import axios from 'axios';
import React, { useEffect, useState } from 'react';

type QueryResult = {
    course_id: string;
    waiting_list_count: number;
};

const QueryLongestWaitingList: React.FC = () => {

    const [queryResult, setQueryResult] = useState<QueryResult | null >(null);

  const fetchData = async () => {
    try {
      const response = await axios.get(
        `http://localhost:8000/course_with_largest_waitlist`
      );
      setQueryResult(response.data.course_with_largest_waitlist);
    } catch (error) {
      console.error("Error fetching chapter details:", error);
    }
  };

  useEffect(() => {
    fetchData();
  }, []);

    return (
        <div>
            {queryResult && (
                <table style={{ border: '1px solid black', borderCollapse: 'collapse', width: '100%' }}>
                    <thead>
                        <tr>
                            <th style={{ border: '1px solid black', padding: '8px' }}>Course ID</th>
                            <th style={{ border: '1px solid black', padding: '8px' }}>Waiting List Count</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td style={{ border: '1px solid black', padding: '8px' }}>{queryResult.course_id}</td>
                            <td style={{ border: '1px solid black', padding: '8px' }}>{queryResult.waiting_list_count}</td>
                        </tr>
                    </tbody>
                </table>
            )}
        </div>
    );
};

export default QueryLongestWaitingList;