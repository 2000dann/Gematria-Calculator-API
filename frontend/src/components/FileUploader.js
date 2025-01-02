import React, { useState } from "react";
import axios from "axios";

const FileUploader = ({ onUploadComplete }) => {
    const [file, setFile] = useState(null);

    const handleFileChange = (e) => {
        setFile(e.target.files[0]);
    };

    const handleUpload = async () => {
        if (!file) {
            alert("Please select a file first.");
            return;
        }
        const formData = new FormData();
        formData.append("file", file);
        try {
            const response = await axios.post("http://127.0.0.1:8000/upload/", formData, {
                headers: {
                    "Content-Type": "multipart/form-data",
                },
            });
            onUploadComplete(response.data);
        } catch (error) {
            console.error("File upload failed:", error);
            alert("Error uploading file.");
        }
    };

    return (
        <div>
            <input type="file" onChange={handleFileChange} />
            <button onClick={handleUpload}>Upload</button>
        </div>
    );
};

export default FileUploader;
