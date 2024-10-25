import { useState } from 'react';
import axios from 'axios';

const TestPage = () => {
    const [data, setData] = useState<string | null>(null);

    const handleButtonClick = async () => {
        try {
            const response = await axios.get('http://localhost:8000/',);
            setData(response.data);
        } catch (error) {
            console.error('Error fetching data:', error);
            setData('Error fetching data');
        }
    };

    return (
        <div>
            <button onClick={handleButtonClick}>Fetch Data</button>
            {data && <div>{data}</div>}
        </div>
    );
};

export default TestPage;