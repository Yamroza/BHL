import axios from 'axios';

const Fetch = axios.create({
    baseURL: "http://localhost:8000/",
    withCredentials: true,
});

export { Fetch };