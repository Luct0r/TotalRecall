                DirectoryEntry directoryObject = new DirectoryEntry
                
                {
                    Path = "LDAP://" + tLDAP
                };

                Match uMatch = Regex.Match(tLDAP, "(?<User>CN=.*)", RegexOptions.IgnoreCase);
                string userDN = uMatch.Groups["User"].ToString();
                string user = userDN.Replace("CN=", "");
                user = user.Substring(0, user.IndexOf(','));
                user = user.ToLower();
                DirectorySearcher subSearcher = new DirectorySearcher(directoryObject)
                {
                    Filter = "(sAMAccountName=" + user + ")"
                };

                SearchResult sResult = subSearcher.FindOne();
                StringBuilder strBuild = new StringBuilder();
                ResultPropertyCollection pCollection = sResult.Properties;
                ICollection iCollection = pCollection.PropertyNames;
                IEnumerator iEnumerator = iCollection.GetEnumerator();
                while (iEnumerator.MoveNext())
                {
                    if (iEnumerator.Current.ToString() == "serviceprincipalname")
                    {
                        strBuild.Append(sResult.Properties[iEnumerator.Current.ToString()][0]);
                    }
                }
////////////////////////////////////////////////////////////////////////////////////////////////////////
                SearchResult sResult = subSearcher.FindOne();
                ResultPropertyCollection pCollection = sResult.Properties;
                ICollection iCollection = pCollection.PropertyNames;
                IEnumerator iEnumerator = iCollection.GetEnumerator();

                string[] strArray = new string[9];
                while (iEnumerator.MoveNext())
                {
                    if (iEnumerator.Current.ToString() == "samaccountname")
                    {
                        strArray.SetValue("---> sAMAccountName                : " + sResult.Properties[iEnumerator.Current.ToString()][0], 0);
                    }
                    if (1==1)
                    {
                            strArray.SetValue("---> Description                   : ", 1);
                    }
                    if (iEnumerator.Current.ToString() == "serviceprincipalname")
                    {
                        strArray.SetValue("---> servicePrincipalName          : " + sResult.Properties[iEnumerator.Current.ToString()][0], 2);
                    }
                    if (iEnumerator.Current.ToString() == "whencreated")
                    {
                        strArray.SetValue("---> whenCreated                   : " + sResult.Properties[iEnumerator.Current.ToString()][0], 3);
                    }
                    if (iEnumerator.Current.ToString() == "whenchanged")
                    {
                        strArray.SetValue("---> whenChanged                   : " + sResult.Properties[iEnumerator.Current.ToString()][0], 4);
                    }
                    if (iEnumerator.Current.ToString() == "useraccountcontrol")
                    {
                        strArray.SetValue("---> userAccountControl            : " + sResult.Properties[iEnumerator.Current.ToString()][0], 5);
                    }
                    if (iEnumerator.Current.ToString() == "msds-supportedencryptiontypes")
                    {
                        strArray.SetValue("---> msds-SupportedEncryptionTypes : " + sResult.Properties[iEnumerator.Current.ToString()][0], 6);
                    }
                    if (iEnumerator.Current.ToString() == "pwdlastset")
                    {
                        long pwdSet = (long)sResult.Properties[iEnumerator.Current.ToString()][0];
                        DateTime dtPwdSet = DateTime.FromFileTime(pwdSet);
                        strArray.SetValue("---> pwdLastSet                    : " + dtPwdSet, 7);
                    }
                    if (iEnumerator.Current.ToString() == "lastlogon")
                    {
                        long LastLogon = (long)sResult.Properties[iEnumerator.Current.ToString()][0];
                        DateTime dtLastLogon = DateTime.FromFileTime(LastLogon);
                        strArray.SetValue("---> lastLogon                     : " + dtLastLogon, 8);
                    }
                }

                Console.WriteLine("User Attributes:");
                Console.WriteLine();
                foreach (string str in strArray)
                {
                    Console.WriteLine(str.ToString());
                }
