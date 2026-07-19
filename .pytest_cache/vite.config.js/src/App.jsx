import { useEffect } from "react";

export default function App() {
  useEffect(() => {
      const script = document.createElement("script");
          script.src = "/script.js";
              script.defer = true;
                  document.body.appendChild(script);

                      return () => {
                            document.body.removeChild(script);
                                };
                                  }, []);

                                    return (
                                        <div>
                                              <h1>BitfuryTech Asset Management</h1>
                                                    <p>React has been successfully integrated.</p>
                                                        </div>
                                                          );
                                                          }