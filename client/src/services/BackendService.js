class BackendService {
    static async transliterateText(prompt) {
        try {
            const apiEndpoint = import.meta.env.VITE_API_ENDPOINT;

            if (!apiEndpoint) {
                throw new Error('API endpoint not specified in the environment variables.');
            }
            const response = await fetch(apiEndpoint + 'transliterate_text', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ prompt }),
            });

            if (!response.ok) {
                throw new Error(`HTTP error! Status: ${response.status}`);
            }

            const data = await response.json();
            return data.result;
        } catch (error) {
            console.error('Error:', error);
            throw error;
        }
    }

    static async getBlogPosts() {
        try {
            const apiEndpoint = import.meta.env.VITE_API_ENDPOINT;

            if (!apiEndpoint) {
                throw new Error('API endpoint not specified in the environment variables.');
            }

            const response = await fetch(apiEndpoint + 'posts/all', {
                method: 'GET',
            });

            if (!response.ok) {
                throw new Error(`HTTP error! Status: ${response.status}`);
            }

            const data = await response.json();
            return data;
        } catch (error) {
            console.error('Error:', error);
            throw error;
        }
    }

    static async createBlogPost(postData, jwtToken) {
        try {
            const apiEndpoint = import.meta.env.VITE_API_ENDPOINT;

            if (!apiEndpoint) {
                throw new Error('API endpoint not specified in the environment variables.');
            }

            const response = await fetch(apiEndpoint + 'posts', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'Authorization': `Bearer ${jwtToken}`, // Injecting JWT token
                },
                body: JSON.stringify(postData),
            });

            if (!response.ok) {
                throw new Error(`HTTP error! Status: ${response.status}`);
            }

            const data = await response.json();
            return data;
        } catch (error) {
            console.error('Error:', error);
            throw error;
        }
    }
}

export default BackendService;