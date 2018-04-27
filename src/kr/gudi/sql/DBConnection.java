package kr.gudi.sql;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.ResultSetMetaData;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;

public class DBConnection {
	private static String url = "jdbc:mysql://192.168.1.229:3306/test";
	private static String user = "root";
	private static String pwd = "1234";
	private static List<HashMap<String, Object>> list = null;
	
	public static Connection openDB() throws Exception {
		Class.forName("org.mariadb.jdbc.Driver");
		return DriverManager.getConnection(url, user, pwd);
	}
	public static List<HashMap<String, Object>> select(Connection con, String sql) throws Exception {
		list = new ArrayList<HashMap<String, Object>>();
		
		PreparedStatement ps = con.prepareStatement(sql);
		ResultSet rs = ps.executeQuery();
		ResultSetMetaData rm = rs.getMetaData();
		while(rs.next()) {
			HashMap<String, Object> map = new HashMap<String, Object>();
			for(int i = 1; i <= rm.getColumnCount(); i++) {
				String column = rm.getColumnName(i);
				Object value = "";
				if("java.lang.String".equals(rm.getColumnClassName(i))) {
					value  = rs.getString(column);
				} else if ("java.lang.Integer".equals(rm.getColumnClassName(i))) {
					value  = rs.getInt(column);
				}
				map.put(column, value);
			}
			list.add(map);
		}
		
		rs.close();
		ps.close();
		
		return list;
	}
	
	public static int edit(Connection con, String sql, List dataList) throws Exception {
		PreparedStatement ps = con.prepareStatement(sql);
		
		for(int i = 1; i <= dataList.size(); i++) {
			ps.setString(i, dataList.get(i-1).toString());
		}
		
		int result = ps.executeUpdate();
		ps.close();
		return result;
	}
	
	public static boolean create(Connection con, String sql) throws Exception {
		PreparedStatement ps = con.prepareStatement(sql);
		return ps.execute();
	}
	
}
