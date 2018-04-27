package kr.gudi.sql;
import java.sql.Connection;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;

public class TestData extends DBConnection {

	static Connection con;
	static List<HashMap<String, Object>> list;
	static String sql;
	
	public static void main(String[] args) throws Exception {
		con = openDB();
		// 1) 값을 입력한다.
		입력();
		// 2) 입력된 값을 확인 한다.
		확인();
		// 3) 입력된 값을 수정 한다.
		수정();
		// 4) 수정한 값을 확인 한다.
		확인();
		// 5) 수정한 값을 삭제 한다.
		삭제();
		// 6) 삭제한 값을 확인 한다.
		확인();
	}
	
	public static void 확인() throws Exception {
		System.out.println("확인()");
		sql = "select * from user";
		list = select(con, sql);
		for(int i = 0; i < list.size(); i++) {
			System.out.println(list.get(i));
		}
	}
	
	public static void 입력() throws Exception {
		System.out.println("입력()");
		sql = "insert into user (id, pass) values (?, ?)";
		List dataList = new ArrayList();
		dataList.add("아이디");
		dataList.add("비밀번호");
		int result = edit(con, sql, dataList);
		System.out.println(result);
	}
	
	public static void 수정() throws Exception {
		System.out.println("수정()");
		sql = "UPDATE user SET pass = ? WHERE id = ?";
		List dataList = new ArrayList();
		dataList.add("수정");
		dataList.add("아이디");
		int result = edit(con, sql, dataList);
		System.out.println(result);
	}
	
	public static void 삭제() throws Exception {
		System.out.println("삭제()");
		sql = "delete from user where id = ?";
		List dataList = new ArrayList();
		dataList.add("아이디");
		int result = edit(con, sql, dataList);
		System.out.println(result);
	}

}
