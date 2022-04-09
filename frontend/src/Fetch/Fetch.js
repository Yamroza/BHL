import axios from 'axios';

const Fetch = axios.create({
    baseURL: "http://localhost:8080/",
    withCredentials: true,
});

export { Fetch };