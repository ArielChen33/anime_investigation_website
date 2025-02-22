import React, {useState, useEffect } from "react";
import axios from "axios";
import { LineChart, Line, XAxis, YAxis, Tooltip, ResponsiveContainer } from "recharts";
import "./AnimeChart.css"

const AnimeChart = () => {

    const [animeData, setAnimeData] = useState([]);

    useEffect(() => {
        axios.get("http://localhost:8000/anime-rankings")
        .then(response => {
            setAnimeData(response.data.data);
            
        })
        .catch(error => console.error("Error fetching data: ", error));
    }, []);

    return (
        <>
        <ResponsiveContainer width="100%" height={400}>
            <LineChart data={animeData}>
                <XAxis dataKey="title"></XAxis>
                <YAxis dataKey="rank" reversed></YAxis>
                <Tooltip/>
                <Line type="monotone" dataKey="rank" stroke="#8884d8"/>
            </LineChart>
        </ResponsiveContainer>

        <table >
            <thead>
                <tr>
                    <th>Title</th>
                    <th>Rank</th>
                    <th>Score</th>
                    <th>Popularity</th>
                </tr>
            </thead>
            {animeData.map(data => (
                <tbody>
                    <tr>
                        <td>{data.title}</td>
                        <td>{data.rank}</td>
                        <td>{data.score}</td>
                        <td>{data.popularity}</td>
                    </tr>
                </tbody>
            ))}
        </table>
        </>
    )
}

export default AnimeChart;