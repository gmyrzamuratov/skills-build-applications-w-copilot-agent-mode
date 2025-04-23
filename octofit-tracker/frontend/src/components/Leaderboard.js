import React, { useEffect, useState } from 'react';

function Leaderboard() {
  const [leaders, setLeaders] = useState([]);
  // -8000.app.github.dev/api/leaderboard
  useEffect(() => {
    fetch('https://laughing-space-invention-jjrrqw595jqh5x4g-8000.app.github.dev/leaderboard/')
      .then(res => res.json())
      .then(data => setLeaders(data));
  }, []);

  return (
    <div className="container mt-4">
      <h1 className="mb-4">Leaderboard</h1>
      <div className="card">
        <div className="card-body">
          <table className="table table-hover">
            <thead>
              <tr>
                <th>#</th>
                <th>Name</th>
                <th>Points</th>
              </tr>
            </thead>
            <tbody>
              {leaders.map((user, idx) => (
                <tr key={idx}>
                  <td>{idx + 1}</td>
                  <td>{user.name}</td>
                  <td>{user.points}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </div>
    </div>
  );
}

export default Leaderboard;
